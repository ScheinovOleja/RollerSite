from django.apps import AppConfig
from cms.apps import CMSConfig as BaseCMSConfig
from django.contrib.auth.apps import AuthConfig
from django.utils.translation import gettext_lazy as _


class LoginConfig(AppConfig):
    name = 'login'
    verbose_name = 'Пользователи'
    verbose_name_plural = _('Пользователи')


class MyAuthConfig(AuthConfig):
    verbose_name = 'Группы'


class CMSConfig(BaseCMSConfig):
    default_auto_field = 'django.db.models.AutoField'
    verbose_name = _('Управление страницами')


class SnippetConfig(AppConfig):
    name = 'djangocms_snippet'
    verbose_name = _('Не трогаем')


class FilerConfig(AppConfig):
    name = 'filer'
    verbose_name = _("Браузер файлов")
