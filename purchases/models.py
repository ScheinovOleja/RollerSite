import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from login.models import MyManager
from orders.models import Order


class Incoming(models.Model):
    date_income = models.DateField(auto_now_add=True, auto_created=True, verbose_name="День дохода")
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=True,
                              verbose_name='Заказ дохода')
    sum = models.FloatField(verbose_name='Сумма дохода')

    class Meta:
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return f'{self.date_income} - {self.order} - {self.sum} руб.'


class Costs(models.Model):
    date_cost = models.DateField(auto_now_add=True, auto_created=True, verbose_name='День расхода')
    note = models.TextField(max_length=256, verbose_name='Примечание')
    sum = models.FloatField(verbose_name='Сумма расхода')

    class Meta:
        verbose_name = 'Расход'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return f'{self.date_cost} - {self.sum} руб.'

    def calc_profitability(self, cost):
        profitability = Profitability.objects.get_or_create(
            month_profitability__month=cost.date_cost.month,
            month_profitability__year=cost.date_cost.year
        )
        profitability[0].costs_in_month += cost.sum
        profitability[0].percent_profitability = round((profitability[0].income_in_month / profitability[
            0].costs_in_month) * 100, 2)
        profitability[0].save()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super(Costs, self).save(force_insert=False, force_update=False, using=None,
                                update_fields=None)
        self.calc_profitability(self)


class Profitability(models.Model):
    class Meta:
        verbose_name = 'Рентабельность'
        verbose_name_plural = 'Рентабельность'

    objects = MyManager()
    month_profitability = models.DateField(auto_now_add=True, auto_created=True, verbose_name='Месяц рентабельности')
    income_in_month = models.FloatField(verbose_name='Общий доход за месяц', null=True, default=0.0)
    costs_in_month = models.FloatField(verbose_name='Общий расход за месяц', null=True, default=0.0)
    percent_profitability = models.FloatField(verbose_name='Процент рентабельности за месяц', null=True, default=0.0)

    def __str__(self):
        all_month = ['', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь',
                     'Ноябрь', 'Декабрь']
        return f'{all_month[self.month_profitability.month]} {self.month_profitability.year} г. - {self.percent_profitability}%'
