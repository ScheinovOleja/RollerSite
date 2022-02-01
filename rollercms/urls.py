from django.urls import path

from rollercms.views import post, wa_bot, blog_get, PostDetailView

urlpatterns = [
    path('vibermsgget/', post),
    path('wamsgget/', wa_bot),
    path('', blog_get, name='all_posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
]
