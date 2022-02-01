from django.db import models

# Create your models here.
from RollerSiteCms import settings
from orders.models import Order


class Review(models.Model):
    CONFIRM_STATUS = (
        (0, 'Отзыв не подтвержден'),
        (1, 'Отзыв одобрен'),
        (2, 'Отзыв отклонен'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Пользователь', on_delete=models.DO_NOTHING)
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, verbose_name='Заказ отзыва')
    review = models.TextField(max_length=5000, verbose_name='Текст отзыва')
    is_confirm = models.IntegerField(choices=CONFIRM_STATUS, default=CONFIRM_STATUS[0][0], verbose_name='Статус отзыва')
