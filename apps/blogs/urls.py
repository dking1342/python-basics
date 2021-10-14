from django.urls import path
from .views import PostDetail, PostList


app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/',PostDetail.as_view(),name='blog'),
    path('',PostList.as_view(),name='blogs'),
]