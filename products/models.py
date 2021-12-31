from django.db import models

# Create your models here.
from login.models import MyManager
from orders.models import Order


class PriceCategory(models.Model):
    class Meta:
        verbose_name = 'Ценовая категория'
        verbose_name_plural = 'Все ценовые категории'

    objects = MyManager()
    name = models.CharField(max_length=2, verbose_name='Ценовая категория', null=False, blank=False)

    def __str__(self):
        return self.name


class GridPrice(models.Model):
    class Meta:
        verbose_name = 'Сеточный прайс'
        verbose_name_plural = 'Все сеточные прайсы'

    objects = MyManager()
    width = models.FloatField('Ширина')
    height = models.FloatField('Высота')
    price = models.FloatField('Цена')
    type_construction = models.ForeignKey('TypeConstruction', on_delete=models.DO_NOTHING,
                                          verbose_name='Тип конструкции', null=False, blank=False)
    price_category = models.ForeignKey(PriceCategory, on_delete=models.DO_NOTHING,
                                       verbose_name='Ценовая категория', null=False, blank=False)

    def __str__(self):
        return f'{self.width}/{self.height} = {self.price}'


class Materials(models.Model):
    class Meta:
        verbose_name = 'Материал'
        verbose_name_plural = 'Все материалы'

    objects = MyManager()
    name = models.CharField(max_length=128, verbose_name='Название материала', null=False, blank=False)
    color = models.CharField('Цвет материала', max_length=32, null=False, blank=False)
    type_construction = models.ForeignKey('TypeConstruction', null=False, blank=False, on_delete=models.DO_NOTHING,
                                          verbose_name='Тип конструкции')

    def __str__(self):
        return f'{self.color}/{self.name}/{self.type_construction}'


class TypeConstruction(models.Model):
    class Meta:
        verbose_name = 'Тип конструкции'
        verbose_name_plural = 'Все типы конструкций'

    objects = MyManager()
    name = models.CharField(max_length=128, verbose_name='Название конструкции', null=False, blank=False)
    is_special = models.BooleanField(default=False, verbose_name='Конструкция без сеточного прайса')

    def __str__(self):
        return self.name


class ControlType(models.Model):
    class Meta:
        verbose_name = 'Тип управления'
        verbose_name_plural = 'Все типы управления'

    objects = MyManager()
    type_control = models.CharField(max_length=128, verbose_name='Тип управления', null=False, blank=False)

    def __str__(self):
        return self.type_control


class MountType(models.Model):
    class Meta:
        verbose_name = 'Тип крепления'
        verbose_name_plural = 'Все типы крепления'

    objects = MyManager()
    mount_type = models.CharField(max_length=128, verbose_name='Тип крепления', null=False, blank=False)

    def __str__(self):
        return self.mount_type


class TypeFabricMeasurement(models.Model):
    class Meta:
        verbose_name = 'Тип замера'
        verbose_name_plural = 'Все типы замеров'

    objects = MyManager()
    type_measurement = models.CharField(max_length=128, verbose_name='Тип замера', null=False, blank=False)

    def __str__(self):
        return self.type_measurement


class HardwareColor(models.Model):
    class Meta:
        verbose_name = 'Цвет фурнитуры'
        verbose_name_plural = 'Все цвета фурнитур'

    objects = MyManager()
    color = models.CharField('Цвет фурнитуры', max_length=32, null=False, blank=False)
    multiplication = models.FloatField('Умножение цены(по умолчанию 1)', null=False, blank=False, default=1)

    def __str__(self):
        return f'{self.color} x{self.multiplication}'


class ProductList(models.Model):
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Все товары'

    objects = MyManager()
    order = models.ForeignKey(Order, on_delete=models.DO_NOTHING, null=False, blank=False,
                              verbose_name='Заказ')
    type_construction = models.ForeignKey(TypeConstruction, on_delete=models.DO_NOTHING, null=False, blank=False,
                                          verbose_name='Тип конструкции')
    material = models.ForeignKey(Materials, on_delete=models.DO_NOTHING, null=False, blank=False,
                                 verbose_name='Материал')
    width = models.FloatField('Ширина', null=False, blank=False)
    height = models.FloatField('Высота', null=False, blank=False)
    count = models.IntegerField('Количество', null=False, blank=False)
    control_type = models.ForeignKey(ControlType, on_delete=models.DO_NOTHING, null=False, blank=False,
                                     verbose_name='Управление')
    control_length = models.FloatField('Длина управления', null=False, blank=False)
    hardware_color = models.ForeignKey(HardwareColor, verbose_name='Цвет фурнитуры', on_delete=models.DO_NOTHING,
                                       null=False, blank=False)
    mount_type = models.ForeignKey(MountType, on_delete=models.DO_NOTHING, null=False, blank=False,
                                   verbose_name='Тип крепления')
    type_of_fabric_measurement = models.ForeignKey(TypeFabricMeasurement, on_delete=models.DO_NOTHING, null=False,
                                                   blank=False, verbose_name='Тип замера по ткани')

    price = models.FloatField('Цена', null=False, blank=False)

    def __str__(self):
        return f'{self.type_construction} - {self.material} - {self.price}'
