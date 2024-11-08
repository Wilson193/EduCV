from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Docente
from django.shortcuts import get_object_or_404 #wilson
from django.http import HttpResponse #wilson
from docx import Document #wilson

def update_teacher(request):
    if request.method == 'POST':
        # Obtén los datos del formulario
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        cedula = request.POST.get('cedula')
        num_telefono = request.POST.get('num_telefono')
        universidad = request.POST.get('universidad')
        cargo = request.POST.get('cargo')
        correo = request.POST.get('correo')
        facultad = request.POST.get('facultad')
        categoria = request.POST.get('categoria')
        especialidad = request.POST.get('especialidad')
        tipo_contrato = request.POST.get('tipo_contrato')
        fecha_contratacion = request.POST.get('fecha_contratacion')

        user = request.user
        # Verifica si el correo ya está registrado en Docente
        try:
            docente = Docente.objects.get(correo=user.email)
        except Docente.DoesNotExist:
            docente = None
        
        if docente:
            # Si el docente ya existe, solo actualizamos sus datos
            docente.nombre = nombre
            docente.apellido = apellido
            docente.cedula = cedula
            docente.num_telefono = num_telefono
            docente.universidad = universidad
            docente.cargo = cargo
            docente.correo = correo
            docente.facultad = facultad
            docente.categoria = categoria
            docente.especialidad = especialidad
            docente.tipo_contrato = tipo_contrato
            docente.fecha_contratacion = fecha_contratacion
            docente.save()

            # Actualizamos también los datos del usuario relacionado
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo  # Actualiza el correo si es necesario
            user.save()

            messages.success(request, "Datos del docente actualizados con éxito.")
        else:
            # Si no se encuentra el docente, creamos uno nuevo
            user.first_name = nombre
            user.last_name = apellido
            user.email = correo  # Actualiza el correo del usuario
            user.save()

            # Crear un nuevo objeto Docente
            docente = Docente(
                user=user,
                nombre=nombre,
                apellido=apellido,
                cedula=cedula,
                num_telefono=num_telefono,
                universidad=universidad,
                cargo=cargo,
                correo=correo,
                facultad=facultad,
                categoria=categoria,
                especialidad=especialidad,
                tipo_contrato=tipo_contrato,
                fecha_contratacion=fecha_contratacion,
            )
            docente.save()

            messages.success(request, "Docente creado con éxito.")

        return redirect('register')

    return render(request, 'register.html')  # La plantilla del formulario de actualización

    