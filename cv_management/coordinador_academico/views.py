from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CoordinadorAcademico
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from docente.models import Docente

# Create your views here.
def update_coordinator(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        num_telefono = request.POST.get('num_telefono')
        universidad = request.POST.get('universidad')
        cargo = request.POST.get('cargo')
        correo = request.POST.get('correo')
        dependencia = request.POST.get('dependencia')
        telefono_oficina = request.POST.get('telefono_oficina')
        oficina = request.POST.get('oficina')

        # Verifica que el correo no esté registrado
        if Docente.objects.filter(correo=correo).exists():
            messages.error(request, "El correo ya está registrado.")
            return redirect('settings')
        
        user = request.user
        user.first_name= nombre
        user.last_name= apellido
        user.save()

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
        return redirect('dashboard')  # O la vista a donde quieras redirigir

    return render(request, 'settings')  # La plantilla del formulario de registro
    

def settings(request):
    return render(request, 'settings.html')
