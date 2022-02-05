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
    list_display = ['num_order', 'get_user_name', 'get_manager_name', 'payment_state', 'cancel_order', 'download_doc']
    fields = ['user', 'payment_state', 'is_cancel', 'extra_charge', 'delivery_price',
              'installation_price', 'terms_of_readiness', 'installation_time', 'note', 'prepayment', 'order_price',
              'contract']
    list_filter = ['payment_state', 'is_cancel']
    readonly_fields = ['payment_state', 'is_cancel', 'cancel_order', 'contract']
    search_fields = ['num_order']
    inlines = [ProductInline, OrderStateInline]
    change_form_template = 'admin/orders/change_form.html'
    form = UserAutocompleteForm

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
        super(OrderAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        try:
            if any([state.cleaned_data['status'] == 2 and not state.cleaned_data['DELETE'] for state in formset]):
                form.instance.payment_state = True
                form.instance.save()
            else:
                form.instance.payment_state = False
                form.instance.save()
        except Exception as err:
            pass
        super().save_formset(request, form, formset, change)

    def response_post_save_add(self, request, obj):
        phone = obj.user.phone
        if '+7' in phone:
            index = 2
        else:
            index = 1
        regex = r'^(8|7)' + phone[index:]
        messenger_user = RegisterFromMessangers.objects.get_or_none(phone=phone)
        viber_text = f'Ваш заказ под номером *{obj.num_order}* на сумму *{obj.order_price} руб.* создан!\n\n'
        tg_text = f'Ваш заказ под номером <code>{obj.num_order}</code> на сумму ' \
                  f'<code>{obj.order_price} руб.</code> создан!\n\n'
        file = self.download(request, obj.pk)
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
        if '+7' in phone:
            index = 2
        else:
            index = 1
        regex = r'^(8|7)' + '(' + phone[index:] + ')'
        messenger_user = RegisterFromMessangers.objects.get_or_none(phone=phone)
        viber_text = f'Статус вашего заказа _{obj.num_order}_ обновился!\n\n*{state.get_status_display()}*\n'
        tg_text = f'Статус вашего заказа _{obj.num_order}_ обновился!\n\n<code>{state.get_status_display()}</code>\n'
        if state.status == 5:
            if not obj.is_notified:
                viber_text = f"Ваш заказ *{obj.num_order}* установлен.\n\nПросим оставить вас отзыв следующим сообщением!\n" \
                             f"*Чтобы оставить отзыв напишите */review* и номер заказа, после чего вводите текст отзыва.*\n\n" \
                             f"Пример:\n\n" \
                             f"/review АА01/01.01.21\nТекст отзыва"
                tg_text = f"Ваш заказ <code>{obj.num_order}</code> установлен.\n\nПросим оставить вас отзыв следующим сообщением!\n" \
                          f"Чтобы оставить отзыв напишите <code>/review</code> и номер заказа, после чего вводите текст отзыва.\n\n" \
                          f"Пример:\n\n" \
                          f"/review АА01/01.01.21\nТекст отзыва"
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
            viber_text += f'\nСрок готовности до {terms_of_readiness}.\n\n' \
                          f'Срок монтажа до {installation_time}.'
            tg_text += f'\nСрок готовности до {terms_of_readiness}.\n\n' \
                       f'Срок монтажа до {installation_time}.'
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
            url = '<span>Заказ отменен</span>'
        else:
            url = f'<a href="{reverse(f"admin:cancel", args=(obj.id,))}">Отменить заказ</a>'
        return mark_safe(url)

    def download_doc(self, obj):
        url = f'<a href="{reverse(f"admin:download", args=(obj.id,))}">Скачать спецификацию</a>'
        return mark_safe(url)

    def get_urls(self):
        urls = super().get_urls()
        shard_urls = [path(r'cancel/<pk>', self.admin_site.admin_view(self.cancel), name="cancel"),
                      path(r'download/<pk>', self.admin_site.admin_view(self.download), name="download")
                      ]
        return shard_urls + urls

    def cancel(self, request, pk):
        order = Order.objects.get(id=pk)
        order.is_cancel = True
        order.save()
        return HttpResponseRedirect(reverse(f'admin:orders_order_changelist'))

    def download(self, request, pk):
        file = get_context(pk)
        return file

    def get_user_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_manager_name(self, obj):
        return f'{obj.manager.first_name} {obj.manager.last_name}'

    get_user_name.short_description = 'Заказчик'
    get_manager_name.short_description = 'Менеджер'
    cancel_order.short_description = 'Отмена заказа'
