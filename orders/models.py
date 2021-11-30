from django.db import models

# Create your models here.
from django.db.models import Max

from RollerSiteCms import settings

STATUSES = (
    (0, 'Выезд на замер'),
    (1, 'Заказ не оплачен'),
    (2, 'Заказ оплачен'),
    (3, 'Заказ в производстве'),
    (4, 'Заказ готов'),
    (5, 'Заказ установлен')
)


def get_new_default():
    if StateOrder.objects.all().count() == 0:
        new_order_default = STATUSES[0][0]
    else:
        new_order_default = StateOrder.objects.all().aggregate(Max('status'))
        index = STATUSES.index(
            (int(new_order_default['status__max']), STATUSES[int(new_order_default['status__max'])][1])
        )
        new_order_default = STATUSES[index + 1][0]
    return new_order_default


class StateOrder(models.Model):
    status = models.CharField(max_length=64, choices=STATUSES, default=get_new_default, verbose_name='Статус заказа')
    date_time = models.DateTimeField(verbose_name='Дата и время статуса', auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Заказ')

    class Meta:
        ordering = ['-date_time']
        verbose_name = 'Статусы заказов'
        verbose_name_plural = 'Статусы заказов'

    def __str__(self):
        return self.status


class Order(models.Model):
    class Meta:
        verbose_name = 'Заказы'
        verbose_name_plural = 'Заказы'

    STATUS_PAYMENT = (
        (True, 'Оплачено'),
        (False, 'Ожидает оплаты'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False, blank=True,
                             verbose_name='Заказчик', limit_choices_to={'is_staff': False})
    num_order = models.CharField(max_length=64, unique=True, verbose_name='Номер заказа')
    order_price = models.FloatField(verbose_name='Сумма заказа')
    payment_state = models.BooleanField(choices=STATUS_PAYMENT, verbose_name='Статус оплаты')
    contract = models.FileField(upload_to='contracts', verbose_name='Договор')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False, blank=True,
                                verbose_name='Менеджер', related_name='manager')

    def __str__(self):
        return self.num_order + '/' + self.user.get_full_name()
