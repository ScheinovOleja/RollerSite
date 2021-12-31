from django.urls import re_path

from .views import ChangePrice, get_materials, get_special_construction

urlpatterns = [
    re_path('counting_price/', ChangePrice.as_view(), name='count_price'),
    re_path('get_material/', get_materials, name='get_material'),
    re_path('get_special_construction/', get_special_construction, name='get_construct')
]
