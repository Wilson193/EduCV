from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from docente.models import Docente  # Asegúrate de importar tu modelo
from coordinador_academico.models import  CoordinadorAcademico  # Asegúrate de importar tu modelo
from accounts.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password  = request.POST.get('password')
        rol = request.POST.get('rol')
        
        #Crear el usuario en la base de datos
        user = User.objects.create_user(email=email, password=password)

        if rol == 'Docente':
            group = Group.objects.get(name='Docente')
            user.groups.add(group)
            #Docente.objects.create(user=user)
        elif rol == 'Coordinador':
            group = Group.objects.get(name='Coordinador')
            user.groups.add(group)
            #CoordinadorAcademico.objects.create(user=user)

        return render(request, 'signup.html')  # O redirigir a otra página

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)   
                 
            if user.groups.filter(name='Docente').exists():
                return redirect('settings')
            elif user.groups.filter(name='Coordinador').exists():
                print("entra al elif")
                return redirect('search')
        else:
            messages.error(request, 'Credenciales inválidas.')
            print(request, 'Credenciales inválidas.')

    return render(request, 'signin.html')

def signout(request):
    logout(request) 
    return render(request, 'signin.html')