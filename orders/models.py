from django.db import models

# Create your models here.
from RollerSiteCms import settings


class StateOrder(models.Model):
    STATUSES = (
        ()
    )

    status = models.CharField(max_length=64, verbose_name='Статус заказа')
    date_time = models.DateTimeField(verbose_name='Дата и время статуса', auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=False, blank=True,
                              verbose_name='Заказ')

    class Meta:
        ordering = ['-date_time']

    def __str__(self):
        return self.status


class Order(models.Model):
    STATUS_PAYMENT = (
        (True, 'Оплачено'),
        (False, 'Ожидает оплаты'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False, blank=True,
                             verbose_name='Заказчик')
    num_order = models.CharField(max_length=64, unique=True, verbose_name='Номер заказа')
    order_price = models.FloatField(verbose_name='Сумма заказа')
    payment_state = models.BooleanField(choices=STATUS_PAYMENT, verbose_name='Статус оплаты')
    contract = models.FileField(upload_to='contracts', verbose_name='Договор')

    def __str__(self):
        return self.num_order
