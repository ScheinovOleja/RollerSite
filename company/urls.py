from django.urls import path

from company.views import ConstructDetailView, test

urlpatterns = [
    path('', test, name='all_construct'),
    path('<int:pk>/', ConstructDetailView.as_view(), name='construct_detail')
]
