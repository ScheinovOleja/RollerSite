from django.db import models

from RollerSiteCms import settings
# Create your models here.
from login.models import MyManager

STATUSES = (
    (0, 'Выезд на замер'),
    (1, 'Заказ не оплачен'),
    (2, 'Заказ оплачен'),
    (3, 'Заказ в производстве'),
    (4, 'Заказ готов'),
    (5, 'Заказ установлен'),
    (6, 'Заказ завершен')
)


class StateOrder(models.Model):
    status = models.IntegerField(choices=STATUSES, default=STATUSES[0][0], null=True, blank=True,
                                 verbose_name='Статус заказа')
    date_time = models.DateTimeField(verbose_name='Дата и время статуса', auto_now_add=True)
    order = models.ForeignKey('Order', on_delete=models.CASCADE, null=True, blank=True,
                              verbose_name='Заказ')

    class Meta:
        ordering = ['-date_time']
        verbose_name = 'Статус заказа'
        verbose_name_plural = 'Все статусы заказов'

    def __str__(self):
        return ''


class Order(models.Model):
    objects = MyManager()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Все заказы'

    CANCEL_STATUS = (
        (True, 'Заказ отменен'),
        (False, 'Заказ действителен'),
    )

    STATUS_PAYMENT = (
        (True, 'Оплачено'),
        (False, 'Ожидает оплаты'),
    )

    create_date = models.DateField(auto_created=True, auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False, blank=False,
                             verbose_name='Заказчик', limit_choices_to={'is_staff': False})
    num_order = models.CharField(max_length=64, unique=True, verbose_name='Номер заказа')
    order_price = models.FloatField(verbose_name='Сумма заказа', default=0.0)
    payment_state = models.BooleanField(choices=STATUS_PAYMENT, default=STATUS_PAYMENT[1][0],
                                        verbose_name='Статус оплаты')
    contract = models.FileField(upload_to='contracts', verbose_name='Договор')
    manager = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=False, blank=True,
                                verbose_name='Менеджер', related_name='manager')
    terms_of_readiness = models.IntegerField(verbose_name='Срок готовности', default=0)
    installation_time = models.IntegerField(verbose_name='Срок монтажа', default=0)
    extra_charge = models.FloatField(verbose_name='Наценка (руб.)', blank=True, null=False, default=0.0)
    delivery_price = models.FloatField(verbose_name='Стоимость доставки (руб.)', blank=True, null=False, default=0.0)
    installation_price = models.FloatField(verbose_name='Стоимость монтажа (руб.)', blank=True, null=False, default=0.0)
    prepayment = models.FloatField(verbose_name='Предоплата', blank=True, null=True, default=0.0)
    is_cancel = models.BooleanField(verbose_name='Статус заказа', choices=CANCEL_STATUS, default=CANCEL_STATUS[1][0])
    is_notified = models.BooleanField(verbose_name='Оповещен ли пользователь в соц сети', default=False)
    note = models.TextField(max_length=512, null=True, blank=True, verbose_name='Примечание')

    def __str__(self):
        return self.num_order + '/' + self.user.get_full_name()
