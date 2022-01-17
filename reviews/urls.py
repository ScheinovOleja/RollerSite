from django.urls import path

from reviews.views import review_get

urlpatterns = [
    path('', review_get, name='review'),
]
