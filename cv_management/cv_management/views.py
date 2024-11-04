# my_project/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'pages/index.html')

def home(request):
    return render(request, 'pages/search.html')

def search(request):
    return render(request, 'pages/search.html')

def settings(request):
    return render(request, 'pages/settings.html')

def signin(request):
    return render(request, 'auth/signin.html')

def signup(request):
    return render(request, 'auth/signup.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')
