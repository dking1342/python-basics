from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# from .models import Accounts


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log in the user
            return redirect("articles:list")
    else:
        form = UserCreationForm()
    return render(request,"accounts/signup.html",{"form":form})
             
def signin_view(request):
    pass
