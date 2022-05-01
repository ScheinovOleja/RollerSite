# Register your models here.
from django.contrib import admin

from purchases.models import Profitability


class ProfitabilityAdmin(admin.ModelAdmin):
    list_display = ['my_month_profitability', 'year_profitability', 'all_income', 'all_costs', 'profit', 'my_percent', ]
    list_display_links = None

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def year_profitability(self, obj):
        return obj.month_profitability.year

    def my_month_profitability(self, obj):
        all_month = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                     'Ноябрь', 'Декабрь']
        return all_month[obj.month_profitability.month]

    def my_percent(self, obj):
        return f'{obj.percent_profitability} %'

    def all_income(self, obj):
        return f'{obj.income_in_month} ₽'

    def all_costs(self, obj):
        return f'{obj.costs_in_month} ₽'

    def profit(self, obj):
        return f'{obj.income_in_month - obj.costs_in_month} ₽'

    year_profitability.short_description = 'Год'
    my_month_profitability.short_description = 'Месяц'
    my_percent.short_description = 'Рентабельность(%)'
    all_income.short_description = 'Приход за месяц'
    all_costs.short_description = 'Расход за месяц'
    profit.short_description = 'Прибыль за месяц'
    year_profitability.admin_order_field = 'month_profitability__year'
    my_month_profitability.admin_order_field = 'month_profitability__month'
    my_percent.admin_order_field = 'percent_profitability'


class IncomeAdmin(admin.ModelAdmin):
    list_display = ['date_income', 'my_sum', 'order']

    def my_sum(self, obj):
        return f'{obj.sum} ₽'

    def delete_queryset(self, request, queryset):
        for income in queryset:
            try:
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
        super(IncomeAdmin, self).delete_queryset(request, queryset)

    def delete_model(self, request, obj):
        profitability = Profitability.objects.get(
            month_profitability__month=obj.date_income.month,
            month_profitability__year=obj.date_income.year
        )
        profitability.income_in_month -= obj.sum
        profitability.percent_profitability = round(
            (profitability.income_in_month / profitability.costs_in_month) * 100, 2)
        profitability.save()
        super(IncomeAdmin, self).delete_model(request, obj)

    my_sum.short_description = 'Сумма'
    my_sum.admin_order_field = 'sum'


class CostAdmin(admin.ModelAdmin):
    list_display = ['date_cost', 'my_sum', 'my_note']

    def my_note(self, obj):
        return f'{obj.note[:100] + "..." if len(obj.note) > 100 else obj.note}'

    def my_sum(self, obj):
        return f'{obj.sum} ₽'

    def delete_queryset(self, request, queryset):
        for cost in queryset:
            profitability = Profitability.objects.get(
                month_profitability__month=cost.date_income.month,
                month_profitability__year=cost.date_income.year
            )
            profitability.costs_in_month -= cost.sum
            profitability.percent_profitability = round(
                (profitability.income_in_month / profitability.costs_in_month) * 100, 2)
            profitability.save()
        super(CostAdmin, self).delete_queryset(request, queryset)

    def delete_model(self, request, obj):
        profitability = Profitability.objects.get(
            month_profitability__month=obj.date_income.month,
            month_profitability__year=obj.date_income.year
        )
        profitability.income_in_month -= obj.sum
        profitability.percent_profitability = round(
            (profitability.income_in_month / profitability.costs_in_month) * 100, 2)
        profitability.save()
        super(CostAdmin, self).delete_model(request, obj)

    my_note.short_description = 'Примечание'
    my_sum.short_description = 'Сумма'
