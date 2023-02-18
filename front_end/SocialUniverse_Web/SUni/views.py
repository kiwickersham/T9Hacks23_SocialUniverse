from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'SUni/home.html')

def contact(request):
    context = {
        'title': 'Contact'
    }
    return render(request, 'SUni/contact.html', context)

def about(request):
    context = {
        'title': 'About'
    }
    return render(request, 'SUni/about.html', context)

def login(request):
    context = {
        'title': 'Login'
    }
    return render(request, 'SUni/login.html', context)

def signup(request):
    context = {
        'title': 'Sign Up'
    }
    return render(request, 'SUni/signup.html', context)

