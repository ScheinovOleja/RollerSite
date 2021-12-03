from django.urls import re_path

from .views import ChangePasswordOrEmail, ChangeAvatar

urlpatterns = [
    re_path('^/?$', ChangePasswordOrEmail.as_view(), name='change_password_or_email'),
    re_path('change_avatar/', ChangeAvatar.as_view(), name='change_avatar')
]
