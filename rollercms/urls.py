from django.urls import path

from .views import post, wa_bot

urlpatterns = [
    path('vibermsgget/', post),
    path('wamsgget/', wa_bot),
]
