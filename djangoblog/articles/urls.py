from django.urls import path
from . import views

app_name = "articles"

urlpatterns = [
    path('<slug:slug>',views.article_details,name="details"),
    path('',views.article_list,name="list"), # named urls for route using the name=
]
