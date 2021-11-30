from datetime import datetime

from django.contrib import admin

# Register your models here.
import orders
from orders.models import Order, StateOrder


class OrderStateInline(admin.StackedInline):
    model = StateOrder
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['num_order', 'get_user_name', 'get_manager_name', 'payment_state']
    fields = ['user', 'order_price', 'payment_state', 'contract']
    list_filter = ['payment_state']
    inlines = [OrderStateInline]

    def get_user_name(self, obj):
        return f'{obj.user.first_name} {obj.user.last_name}'

    def get_manager_name(self, obj):
        return f'{obj.manager.first_name} {obj.manager.last_name}'

    def delete_queryset(self, request, queryset):
        for order in queryset:
            for state in order.stateorder_set.all():
                state.delete()
            order.delete()
        super(OrderAdmin, self).delete_queryset(request, queryset)

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
            obj.save()
            StateOrder.objects.create(
                order=obj
            )
        super(OrderAdmin, self).save_model(request, obj, form, change)

    def save_formset(self, request, form, formset, change):
        if not change:
            last_order_for_current_manager = Order.objects.filter(stateorder__date_time__day=datetime.now().date().day,
                                                                  stateorder__date_time__month=datetime.now().date().month,
                                                                  stateorder__date_time__year=datetime.now().date().year
                                                                  ).last()
            if last_order_for_current_manager is None:
                initials_manager = "".join(word[0].upper() for word in request.user.get_full_name().split())
                form.instance.num_order = f'{initials_manager}01/{datetime.now().date().strftime("%d.%m.%y")}'

            else:
                date = last_order_for_current_manager.num_order.split('/')[1]
                number = last_order_for_current_manager.num_order.split('/')[0]
                initials = "".join(word for word in number if word.isalpha())
                new_number = f'{int("".join(word for word in number if word.isdigit())) + 1}'.split()
                if len(new_number) == 1:
                    new_number.insert(0, '0')
                new_number = initials + ''.join(word for word in new_number)
                form.instance.num_order = f'{new_number}/{date}'
            form.instance.manager = request.user
            form.instance.save()
            StateOrder.objects.create(
                order=form.instance
            )
        else:
            try:
                if any([state.cleaned_data['status'] == 'Заказ оплачен' and not state.cleaned_data['DELETE'] for state in formset]):
                    form.instance.payment_state = True
                else:
                    form.instance.payment_state = False
            except:
                pass
            form.instance.save()
        super().save_formset(request, form, formset, change)

    get_user_name.short_description = 'Заказчик'
    get_manager_name.short_description = 'Менеджер'


admin.site.register(Order, OrderAdmin)
# admin.site.register(StateOrder, OrderStateAdmin)
