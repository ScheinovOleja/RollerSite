from django.apps import AppConfig
from cms.apps import CMSConfig as BaseCMSConfig


class LoginConfig(AppConfig):
    name = 'login'
    verbose_name = 'Пользователи'
    verbose_name_plural = 'Пользователи'


class CMSConfig(BaseCMSConfig):
    default_auto_field = 'django.db.models.AutoField'
