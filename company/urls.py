from django.urls import path, re_path

from company.views import ConstructDetailView, test

urlpatterns = [
    re_path('', test, name='all_construct'),
    re_path('<int:pk>/', ConstructDetailView.as_view(), name='construct_detail')
]
