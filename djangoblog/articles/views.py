from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from django.http import HttpResponse

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("date")
    payload = {"articles":articles}
    return render(request,"articles/article_list.html",payload)

def article_details(request,slug):
    # article = Article.objects.get("slug",str(slug))
    # payload = {"article":article}
    # print(article)
    # return render(request,"articles/article_details.html")
    return HttpResponse(f"{slug}")