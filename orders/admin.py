import os
from datetime import datetime

from django.contrib import admin, messages
# Register your models here.
from django.forms import BaseInlineFormSet
from django.http import HttpResponseRedirect
from django.urls import path, reverse
from django.utils.safestring import mark_safe

from login.models import RegisterFromMessangers
from orders.forms import UserAutocompleteForm
from orders.general_func import date_by_add
from orders.import_to_doc import get_context
from orders.models import Order, StateOrder, STATUSES
from products.forms import ProductListAutocompleteForm
from products.models import ProductList
from purchases.models import Incoming, Profitability
from social_treatment.mailing import send_order


class MyOrderFormSet(BaseInlineFormSet):
    @property
    def empty_form(self):
        form = super(MyOrderFormSet, self).empty_form
        try:
            all_status = [my_form.initial['status'] for my_form in self.forms]
            new_state = max(all_status)
        except ValueError as err:
            new_state = -1
        except KeyError as err:
            new_state = -1
        form.fields['status'].initial = new_state + 1
        return form


class MyProductFormSet(BaseInlineFormSet):
    @property
    def empty_form(self):
        form = super(MyProductFormSet, self).empty_form
        return form


class OrderStateInline(admin.TabularInline):
    formset = MyOrderFormSet
    model = StateOrder
    extra = 0

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        if not obj:
            return False
        if obj.stateorder_set.all().count() >= 6 or obj.is_cancel:
            return False
        else:
            return True

    def has_delete_permission(self, request, obj=None):
        if not obj:
            return False
        if obj.stateorder_set.all().count() >= 6 or obj.is_cancel:
            return False
        else:
            return True


class ProductInline(admin.StackedInline):
    formset = MyProductFormSet
    model = ProductList
    extra = 0
    template = 'admin/orders/stacked.html'
    form = ProductListAutocompleteForm


class OrderAdmin(admin.ModelAdmin):
    list_display = ['num_order', 'get_user_name', 'get_manager_name', 'payment_state', 'status_display',
                    'next_status_display', 'cancel_order', 'download_doc']
    fields = ['user', 'payment_state', 'is_cancel', 'extra_charge', 'delivery_price',
              'installation_price', 'terms_of_readiness', 'installation_time', 'note', 'prepayment', 'order_price']
    list_filter = ['payment_state', 'is_cancel']
    readonly_fields = ['payment_state', 'is_cancel', 'cancel_order']
    search_fields = ['num_order']
    inlines = [ProductInline, OrderStateInline]
    change_form_template = 'admin/orders/change_form.html'
    form = UserAutocompleteForm
    date_hierarchy = 'create_date'

    def delete_queryset(self, request, queryset):
        for order in queryset:
            all_income = Incoming.objects.filter(order=order)
            for income in all_income:
                profitability = Profitability.objects.get(
                    month_profitability__month=income.date_income.month,
                    month_profitability__year=income.date_income.year
                )
                profitability.income_in_month -= income.sum
                profitability.percent_profitability = round(
                    (profitability.income_in_month / profitability.costs_in_month) * 100, 2)
                profitability.save()
        super(OrderAdmin, self).delete_queryset(request, queryset)

    def delete_model(self, request, obj):
        try:
            all_income = Incoming.objects.filter(order=obj)
            for income in all_income:
                profitability = Profitability.objects.get(
                    month_profitability__month=income.date_income.month,
                    month_profitability__year=income.date_income.year
                )
                profitability.income_in_month -= income.sum
                profitability.percent_profitability = round(
                    (profitability.income_in_month / profitability.costs_in_month) * 100, 2)
                profitability.save()
        except Exception as err:
            pass
        super(OrderAdmin, self).delete_model(request, obj)

    def calc_profitability(self, income):
        profitability = Profitability.objects.get_or_create(
            month_profitability__month=income.date_income.month,
            month_profitability__year=income.date_income.year
        )
        profitability[0].income_in_month += income.sum
        try:
            profitability[0].percent_profitability = round((profitability[0].income_in_month / profitability[
                0].costs_in_month) * 100, 2)
        except ZeroDivisionError:
            profitability[0].percent_profitability = 0
        profitability[0].save()

    def add_prepayment_income(self, obj):
        income = Incoming.objects.create(
            order=obj,
            sum=obj.prepayment
        )
        self.calc_profitability(income)

    def add_income(self, obj):
        income = Incoming.objects.create(
            order=obj,
            sum=obj.order_price - obj.prepayment
        )
        self.calc_profitability(income)

    def change_view(self, request, object_id, form_url='', extra_context=None):
        order = Order.objects.get(id=object_id)
        state = order.stateorder_set.all().first()
        extra_context = extra_context or {}
        if state.status == 5:
            for field in self.get_fields(request, order):
                if field not in self.readonly_fields:
                    self.readonly_fields.append(field)
            return super(OrderAdmin, self).change_view(request, object_id, extra_context=extra_context)
        if order.is_cancel:
            for field in self.get_fields(request, order):
                if field not in self.readonly_fields:
                    self.readonly_fields.append(field)
        else:
            self.readonly_fields.clear()
            for field in ['payment_state', 'is_cancel', 'cancel_order']:
                self.readonly_fields.append(field)
        return super(OrderAdmin, self).change_view(request, object_id, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        if not change:
            last_order_for_current_manager = Order.objects.filter(stateorder__date_time__day=datetime.now().date().day,
                                                                  stateorder__date_time__month=datetime.now().date().month,
                                                                  stateorder__date_time__year=datetime.now().date().year
                                                                  ).last()
            if last_order_for_current_manager is None:
                initials_manager = "".join(word[0].upper() for word in request.user.get_full_name().split())
                obj.num_order = f'{initials_manager}01/{datetime.now().date().strftime("%d.%m.%y")}'
            else:
                date = last_order_for_current_manager.num_order.split('/')[1]
                number = last_order_for_current_manager.num_order.split('/')[0]
                initials = "".join(word for word in number if word.isalpha())
                new_number = f'{int("".join(word for word in number if word.isdigit())) + 1}'.split()
                if len(new_number) == 1:
                    new_number.insert(0, '0')
                new_number = initials + ''.join(word for word in new_number)
                obj.num_order = f'{new_number}/{date}'
            obj.manager = request.user
            try:
                obj.save()
            except Exception as err:
                messages.error(request, 'Error message')
                return
            StateOrder.objects.create(
                status=STATUSES[0][0],
                order=obj
            )
            StateOrder.objects.create(
                status=STATUSES[1][0],
                order=obj
            )
        if obj.prepayment == 0:
            pass
        else:
            self.add_prepayment_income(obj)
        super(OrderAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        try:
            if any([state.cleaned_data['status'] == 2 and not state.cleaned_data['DELETE'] for state in formset]):
                form.instance.payment_state = True
                form.instance.save()
                self.add_income(form.instance)
            else:
                form.instance.payment_state = False
                form.instance.save()
        except Exception as err:
            pass
        super().save_formset(request, form, formset, change)

    def response_post_save_add(self, request, obj):
        phone = obj.user.phone
        messenger_user = RegisterFromMessangers.objects.get_or_none(phone=phone)
        viber_text = f'?????? ?????????? ?????? ?????????????? *{obj.num_order}* ???? ?????????? *{obj.order_price} ??????.* ????????????!\n\n'
        tg_text = f'?????? ?????????? ?????? ?????????????? <code>{obj.num_order}</code> ???? ?????????? ' \
                  f'<code>{obj.order_price} ??????.</code> ????????????!\n\n'
        self.download(request, obj.pk)
        file = open(os.path.abspath(f'media/contracts/Spec_{obj.num_order.replace("/", "_")}.docx'), 'rb')
        try:
            if obj.user.preferred_social_network == 0:
                send_order(phone=phone, messenger_user=messenger_user, text=tg_text, file=file)
            else:
                send_order(phone=phone, messenger_user=messenger_user, text=viber_text, file=file)
        except Exception as err:
            print(err)
        return super().response_post_save_add(request, obj)

    def response_post_save_change(self, request, obj):
        state = obj.stateorder_set.all().first()
        phone = obj.user.phone
        messenger_user = RegisterFromMessangers.objects.get_or_none(phone=phone)
        viber_text = f'???????????? ???????????? ???????????? _{obj.num_order}_ ??????????????????!\n\n*{state.get_status_display()}*\n'
        tg_text = f'???????????? ???????????? ???????????? _{obj.num_order}_ ??????????????????!\n\n<code>{state.get_status_display()}</code>\n'
        if state.status == 5:
            if not obj.is_notified:
                viber_text = f"?????? ?????????? *{obj.num_order}* ????????????????????.\n\n???????????? ???????????????? ?????? ?????????? ?????????????????? ????????????????????!\n" \
                             f"*?????????? ???????????????? ?????????? ???????????????? */review* ?? ?????????? ????????????, ?????????? ???????? ?????????????? ?????????? ????????????.*\n\n" \
                             f"????????????:\n\n" \
                             f"/review ????01/01.01.21\n?????????? ????????????"
                tg_text = f"?????? ?????????? <code>{obj.num_order}</code> ????????????????????.\n\n???????????? ???????????????? ?????? ?????????? ?????????????????? ????????????????????!\n" \
                          f"?????????? ???????????????? ?????????? ???????????????? <code>/review</code> ?? ?????????? ????????????, ?????????? ???????? ?????????????? ?????????? ????????????.\n\n" \
                          f"????????????:\n\n" \
                          f"/review ????01/01.01.21\n?????????? ????????????"
                obj.is_notified = True
                obj.save()
                if obj.user.preferred_social_network == 0:
                    send_order(phone=phone, messenger_user=messenger_user, text=tg_text)
                else:
                    send_order(phone=phone, messenger_user=messenger_user, text=viber_text)
            return super().response_post_save_change(request, obj)
        if obj.terms_of_readiness or obj.installation_time:
            terms_of_readiness = date_by_add(obj.terms_of_readiness)
            installation_time = date_by_add(obj.installation_time)
            viber_text += f'\n???????? ???????????????????? ???? {terms_of_readiness}.\n\n' \
                          f'???????? ?????????????? ???? {installation_time}.'
            tg_text += f'\n???????? ???????????????????? ???? {terms_of_readiness}.\n\n' \
                       f'???????? ?????????????? ???? {installation_time}.'
        try:
            if obj.user.preferred_social_network == 0:
                send_order(phone=phone, messenger_user=messenger_user, text=tg_text)
            else:
                send_order(phone=phone, messenger_user=messenger_user, text=viber_text)
        except Exception as err:
            pass
        return super().response_post_save_change(request, obj)

    def cancel_order(self, obj):
        if obj.is_cancel:
            url = '<span>?????????? ??????????????</span>'
        else:
            url = f'<a href="{reverse(f"admin:cancel", args=(obj.id,))}">???????????????? ??????????</a>'
        return mark_safe(url)

    def download_doc(self, obj):
        url = f'<a href="{reverse(f"admin:download", args=(obj.id,))}">?????????????? ????????????????????????</a>'
        return mark_safe(url)

    def status_display(self, obj):
        state = obj.stateorder_set.first()
        url = f'<span>{state.get_status_display()}</span>'
        return mark_safe(url)

    def next_status_display(self, obj):
        state = obj.stateorder_set.first()
        try:
            url = f'<a href="{reverse(f"admin:next_status", args=(state.id,))}">{STATUSES[state.status + 1][1]}</a>'
        except IndexError:
            url = '<span>?????????? ????????????????</span>'
        return mark_safe(url)

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [path(r'cancel/<pk>', self.admin_site.admin_view(self.cancel), name="cancel"),
                      path(r'download/<pk>', self.admin_site.admin_view(self.download), name="download"),
                      path(r'next_status/<pk>', self.admin_site.admin_view(self.next_status), name='next_status')
                      ]
        return shard_urls + urls

    def cancel(self, request, pk):
        order = Order.objects.get(id=pk)
        order.is_cancel = True
        order.save()
        phone = order.user.phone
        messenger_user = RegisterFromMessangers.objects.get_or_none(phone=phone)
        viber_text = f'?????? ?????????? *{order.num_order}* ??????????????! ???????? ???? ???? ???????????????? ??????????, ???????????? ???????????????????? ?? ' \
                     f'??????????????????????????!'
        tg_text = f'?????? ?????????? <code>{order.num_order}</code> ??????????????! ???????? ???? ???? ???????????????? ??????????, ???????????? ???????????????????? ?? ' \
                  f'??????????????????????????!'
        if order.user.preferred_social_network == 0:
            send_order(phone=phone, messenger_user=messenger_user, text=tg_text)
        else:
            send_order(phone=phone, messenger_user=messenger_user, text=viber_text)
        return HttpResponseRedirect(reverse(f'admin:orders_order_changelist'))

    def download(self, request, pk):
        file = get_context(pk)
        return file

    def next_status(self, request, pk):
        current_state = StateOrder.objects.get(pk=pk)
        StateOrder.objects.create(
            status=STATUSES[current_state.status + 1][0],
            order=current_state.order
        )
        if not current_state.order.payment_state:
            current_state.order.payment_state = True
            current_state.order.save()
            self.add_income(current_state.order)
        self.response_post_save_change(request, current_state.order)
        return HttpResponseRedirect(reverse(f'admin:orders_order_changelist'))

    def get_user_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_manager_name(self, obj):
        return f'{obj.manager.first_name} {obj.manager.last_name}'

    get_user_name.short_description = '????????????????'
    get_manager_name.short_description = '????????????????'
    cancel_order.short_description = '???????????? ????????????'
    download_doc.short_description = '????????????????????????'
    status_display.short_description = '?????????????? ????????????'
    next_status_display.short_description = '?????????????????? ????????????'
