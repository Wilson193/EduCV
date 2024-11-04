from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from docente.models import Docente  # Asegúrate de importar tu modelo

def signin(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        password = request.POST.get('password')

        try:
            print("mostrar datos")
            print(user = Docente.objects.get(cedula=cedula)) # Buscar por cédula
        except Docente.DoesNotExist:
            user = None

        if user and user.clave == password:  # Comparar la contraseña
            login(request, user)  # Iniciar sesión
            return redirect('nombre_de_la_vista_deseada')
        else:
            print(request, 'Credenciales inválidas.')

    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

