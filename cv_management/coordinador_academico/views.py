from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CoordinadorAcademico
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# Create your views here.
def register_coordinator(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        num_telefono = request.POST.get('num_telefono')
        universidad = request.POST.get('universidad')
        cargo = request.POST.get('cargo')
        correo = request.POST.get('correo')
        clave = request.POST.get('clave')
        dependencia = request.POST.get('dependencia')
        telefono_oficina = request.POST.get('telefono_oficina')
        oficina = request.POST.get('oficina')

        # Verifica que el correo no esté registrado
        if User.objects.filter(email=correo).exists():
            messages.error(request, "El correo ya está registrado.")
            return redirect('register_coordinator')

        # Crea un nuevo usuario para el coordinador
        user = User.objects.create(
            username=cedula,  # Usamos la cédula como nombre de usuario
            email=correo,
            password=make_password(clave),  # Encripta la contraseña
        )

        # Crea un nuevo objeto CoordinadorAcademico
        coordinador = CoordinadorAcademico(
            user=user,
            cedula=cedula,
            nombre=nombre,
            apellido=apellido,
            num_telefono=num_telefono,
            universidad=universidad,
            cargo=cargo,
            dependencia=dependencia,
            telefono_oficina=telefono_oficina,
            oficina=oficina,
        )
        coordinador.save()

        messages.success(request, "Coordinador registrado con éxito.")
        return redirect('login')  # O la vista a donde quieras redirigir

    return render(request, 'register_coordinator.html')  # La plantilla del formulario de registro
    

def settings(request):
    return render(request, 'settings.html')
