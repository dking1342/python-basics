from django.shortcuts import redirect, render
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by("date")
    payload = {"articles":articles}
    return render(request,"articles/article_list.html",payload)

def article_details(request,slug):
    article = Article.objects.get(slug=slug)
    payload = {"article":article}
    return render(request,"articles/article_details.html",payload)

@login_required(login_url="/accounts/signin/")
def article_create(request):
    if request.method == "POST":
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid():
            # save to db
            return redirect("articles:list")
    else:
        form = forms.CreateArticle()
    return render(request,"articles/article_create.html",{"form":form})