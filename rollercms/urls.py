from django.urls import path

from .views import viber_bot, wa_bot

urlpatterns = [
    path('vibermsgget/', viber_bot),
    path('wamsgget/', wa_bot),
]