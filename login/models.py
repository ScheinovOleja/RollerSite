from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

# Create your models here.
from .managers import UserManager


class MyUser(AbstractBaseUser, PermissionsMixin):
    phone_regex = RegexValidator(regex=r'^((8|\+7)[\-]?)?(\(?\d{3}\)?[\-]?)?[\d\-]{7,10}$',
                                 message="Номер телефона в формате 89123456789")
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True, unique=True,
                             verbose_name='Номер телефона')
    email = models.EmailField(unique=True, blank=True, verbose_name='Почта заказчика')
    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    patronymic = models.CharField(max_length=40, blank=True, verbose_name='Отчество')
    address = models.CharField(max_length=255, blank=True, verbose_name='Адрес заказчика')
    avatar = models.TextField('Аватар', max_length=99999)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    class Meta:
        verbose_name = _('Пользователь')
        verbose_name_plural = _('Пользователи')
        permissions = (
            ("can_edit", "Может редактировать страницы"),
            ("can_manager", "Имеет доступ на страницы менеджеров"),
        )

    def __str__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def save(self, *args, **kwargs):
        super(MyUser, self).save(*args, **kwargs)
        return self
