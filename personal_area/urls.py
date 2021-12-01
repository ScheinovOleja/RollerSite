from django.urls import path, re_path

from .views import ChangeAvatar

urlpatterns = [
    re_path('^/?$', ChangeAvatar.as_view(), name='change_avatar'),
]
