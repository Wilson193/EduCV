from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CoordinadorAcademico
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse


def settings(request):
    return render(request, 'settings.html')

def reset_password(request):
    if request.method == 'POST':
        current_password = request.POST.get('current-password')
        new_password = request.POST.get('new-password')
        
        user = request.user
        
        # Verifica si la contraseña actual es correcta utilizando check_password
        if check_password(current_password, user.password):
            # Si la contraseña actual es correcta, actualiza la nueva contraseña
            user.set_password(new_password)
            user.save()
            messages.success(request, "Contraseña actualizada con éxito.")
        else:
            messages.error(request, "La contraseña actual es incorrecta.")
        
        return redirect('settings')
    
    return render(request, 'settings.html')  # La plantilla del formulario de registro

@login_required
def update_picture_coordinator(request):
    if request.method == "POST":
        coordinador = request.user.coordinador_academico
        photo = request.FILES.get('profile_picture_coordinator')
        if photo: 
            coordinador.foto = photo
            coordinador.save()
            return redirect('settings')  # Cambia el nombre según la vista deseada
        if request.POST.get('remove_picture_coordinator') == 'true':
            coordinador.foto.delete(save=True)
            return redirect('settings')
    return HttpResponse("Método no permitido o no se ha subido una imagen", status=400)    
        
        
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

        user = request.user
        # Verifica si el correo ya está registrado en CoordinadorAcademico
        try:
            coordinador = CoordinadorAcademico.objects.get(correo=user.email)
        except CoordinadorAcademico.DoesNotExist:
            coordinador = None
        
        if coordinador:
            # Si el coordinador ya existe, solo actualizamos sus datos
            coordinador.cedula = cedula
            coordinador.nombre = nombre
            coordinador.apellido = apellido
            coordinador.num_telefono = num_telefono
            coordinador.universidad = universidad
            coordinador.cargo = cargo
            coordinador.correo = correo
            coordinador.dependencia = dependencia
            coordinador.telefono_oficina = telefono_oficina
            coordinador.oficina = oficina
            coordinador.save()

            # Actualizamos también los datos del usuario relacionado
            user = coordinador.user
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo  # Actualiza el correo si es necesario
            user.save()

            messages.success(request, "Datos del coordinador actualizados con éxito.")
        else:
            # Si no se encuentra el coordinador, creamos uno nuevo
            user = request.user
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo  # Si es necesario, puedes actualizar el correo del usuario
            user.save()

            # Crear un nuevo objeto CoordinadorAcademico
            coordinador = CoordinadorAcademico(
                user=user,
                cedula=cedula,
                nombre=nombre,
                apellido=apellido,
                num_telefono=num_telefono,
                universidad=universidad,
                cargo=cargo,
                correo = correo,
                dependencia=dependencia,
                telefono_oficina=telefono_oficina,
                oficina=oficina,
            )
            print("esta intentando crearlo")
            coordinador.save()

            messages.success(request, "Coordinador creado con éxito.")

        messages.success(request, "Coordinador modificado con éxito.")
        return redirect('settings')

    return render(request, 'settings.html')  # La plantilla del formulario de registro