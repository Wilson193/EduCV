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
    experiencia = get_object_or_404(ExperienciaLaboral, id=experiencia_id)

    experiencia.delete()

    return redirect('update') 

def register_academicbackground(request):
    if request.method == 'POST':
        nivel = request.POST.get('nivel')
        institucion = request.POST.get('institucion')
        titulo = request.POST.get('titulo')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        ciudad = request.POST.get('ciudad')
        pais = request.POST.get('pais')
        
        user = request.user
        cv = user.docente.cv_docente 
        
        # Guardar en la base de datos
        nueva_formacion = FormacionAcademica(
            cv = cv,
            nivel=nivel,
            institucion=institucion,
            titulo=titulo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            ciudad=ciudad,
            pais=pais
        )
        nueva_formacion.save()
        
        return redirect('update')  # Cambia 'alguna_vista' por la URL que corresponda
    return render(request, 'update.html')

def remove_academic_background(request, formacion_id):
    # Obtener la formación académica que se quiere eliminar
    formacion = get_object_or_404(FormacionAcademica, id=formacion_id)

    # Eliminar la formación académica
    formacion.delete()
    return redirect('update')  


    


@login_required
def privacidad(request):
    
    return render(request, 'pages/privacidad.html')
# Create your views here.
