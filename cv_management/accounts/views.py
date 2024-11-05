from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from docente.models import Docente  # Asegúrate de importar tu modelo

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

