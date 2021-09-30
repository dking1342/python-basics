from django.shortcuts import render
# from .models import Accounts


# Create your views here.
def signup_view(request):
    return render(request,"accounts/signup.html")

def register_view(request):
    return render(request,"accounts/signup.html")
