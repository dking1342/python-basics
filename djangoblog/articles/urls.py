from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>',views.article_details),
    path('',views.article_list),
]
