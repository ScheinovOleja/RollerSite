from django.apps import AppConfig
from cms.apps import CMSConfig as BaseCMSConfig
from django.utils.translation import gettext_lazy as _


class LoginConfig(AppConfig):
    name = 'login'
    verbose_name = 'Пользователи и группы'
    verbose_name_plural = _('Пользователи и группы')


class CMSConfig(BaseCMSConfig):
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = _('Управление страницами')


class SnippetConfig(AppConfig):
    name = 'djangocms_snippet'
    verbose_name = _('Фрагменты HTML')
