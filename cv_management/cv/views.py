from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone

def index(request):
  template = loader.get_template('users.html')
  return HttpResponse(template.render())

def list_cvs(request):
  template = loader.get_template('teachers.html')
  return HttpResponse(template.render())

def consult(request):
    return render(request, 'consult.html')

def modify_privacy(request):
    return render(request, 'modify-privacy.html')

def create(request):
    if request.method == "POST":  # Corregido a comillas simples
        user = request.user
        docente = user.docente
        
        # Crear el CV asociado al docente
        nuevo_cv = CV.objects.create(docente=docente, fecha_creacion=timezone.now(), estado=1)
        
        # Redirige a la página de actualización del CV
        return redirect('update')  # Asegúrate de tener esta URL en urls.py
        
    return render(request, 'create.html')

  
def update(request):
    return render(request, 'update.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ExperienciaLaboral

def register_experience(request):
    if request.method == "POST":
        # Recoger los datos del formulario
        empresa = request.POST.get('empresa')  # 'empresa' es el nombre del campo en el formulario
        cargo = request.POST.get('cargo')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        descripcion = request.POST.get('descripcion')
        
        # Obtener el usuario y el CV relacionado con el docente
        user = request.user
        cv = user.docente.cv_docente  # Usando el related_name

        
        print(f"el valor de cv{cv}")
        
        # Crear la nueva experiencia laboral
        nueva_experiencia = ExperienciaLaboral(
            cv=cv,  # Asociar la experiencia con el CV
            lugar_trabajo=empresa,
            cargo=cargo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            descripcion=descripcion,
        )
        
        # Guardar la nueva experiencia en la base de datos
        nueva_experiencia.save()

        # Mostrar un mensaje de éxito
        messages.success(request, "Experiencia laboral registrada correctamente.")

        # Redirigir a una página, por ejemplo, a la vista del CV o detalles del CV
        return redirect('update')

    return render(request, 'update.html')

def remove_experience(request, experiencia_id):
    # Obtener la experiencia laboral que se quiere eliminar
    experiencia = get_object_or_404(ExperienciaLaboral, id=experiencia_id)

    # Eliminar la experiencia laboral
    experiencia.delete()

    # Redirigir a la página principal o a la lista de experiencias laborales
    return redirect('update')  # Cambia el nombre de la vista a la que corresponda

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import FormacionAcademica

def register_academicbackground(request):
    if request.method == "POST":
        # Recoger los datos del formulario
        nivel = request.POST.get('nivel')
        institucion = request.POST.get('institucion')
        titulo = request.POST.get('titulo')
        fecha_obtencion = request.POST.get('fecha_obtencion')

        # Obtener el usuario y el CV relacionado con el docente
        user = request.user
        cv = user.docente.cv_docente  # Asumiendo que el docente tiene un CV asociado
        
        # Crear la nueva formación académica
        nueva_formacion = FormacionAcademica(
            cv=cv,  # Asociar la formación con el CV
            nivel=nivel,
            institucion=institucion,
            titulo=titulo,
            fecha_obtencion=fecha_obtencion,
        )

        # Guardar la nueva formación académica en la base de datos
        nueva_formacion.save()

        # Mostrar un mensaje de éxito
        messages.success(request, "Formación académica registrada correctamente.")

        # Redirigir a una página, por ejemplo, a la vista del CV o detalles del CV
        return redirect('update')  # Cambia 'update_cv' por la URL que desees

    return render(request, 'update.html')  # Página donde se muestra el formulario

    


@login_required
def privacidad(request):
    
    return render(request, 'pages/privacidad.html')
# Create your views here.
