from django.urls import re_path

from .views import ChangePasswordOrEmail, ChangeAvatar, ChangePreferredNetwork

urlpatterns = [
    re_path('^/?$', ChangePasswordOrEmail.as_view(), name='change_password_or_email'),
    re_path('change_avatar/', ChangeAvatar.as_view(), name='change_avatar'),
    re_path('change_social_network/', ChangePreferredNetwork.as_view(), name='change_social_network')
]
