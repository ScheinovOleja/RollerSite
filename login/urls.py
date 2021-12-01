from django.urls import path

from login import views

urlpatterns = [
    path('auth/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout')
]
