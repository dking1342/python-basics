from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# from .models import Accounts


# Create your views here.
def signup_view(request):
    form = UserCreationForm()
    return render(request,"accounts/signup.html",{"form":form})

def register_view(request):
    return render(request,"accounts/signup.html")
