# my_project/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'pages/index.html')

def home(request):
    return render(request, 'pages/search.html')

def search(request):
    return render(request, 'pages/search.html')

def signin(request):
    return render(request, 'auth/signin.html')

def signup(request):
    return render(request, 'auth/signup.html')

@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')

def resetpassword(request):
    return render(request, 'pages/reset-password.html')

def custom_404_view(request, exception):
    return render(request, 'pages/404.html', status=404)

#def privacidad(request):
#    return render(request, 'pages/privacidad.html')

#def consultar(request):
#    return render(request, 'pages/mostrarcv.html')

#def registrar(request):
#    return render(request, 'pages/registrar.html')