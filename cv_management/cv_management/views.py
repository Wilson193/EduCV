from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from cv.views import notification_view

def index(request):
    return render(request, 'pages/index.html')

def signin(request):
    return render(request, 'auth/signin.html')

def signup(request):
    return render(request, 'auth/signup.html')

def resetpassword(request):
    return render(request, 'pages/reset-password.html')

def custom_404_view(request, exception):
    return render(request, 'pages/404.html', status=404)

