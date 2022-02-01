from django.urls import re_path, path

from letter.views import get_send, send_tg_mail

urlpatterns = [
    path('', get_send, name='get_letter'),
    path('send_tg/', send_tg_mail, name='send_tg')
]
