from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.http import HttpResponse #wilson
from docx import Document #wilson
from docx.oxml import OxmlElement#wilson
from docx.oxml.ns import qn #wilson
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx.shared import Pt


def index(request):
  template = loader.get_template('users.html')
  return HttpResponse(template.render())

@login_required
def teachers(request):
  return render(request, 'teachers.html')

@login_required
def consult(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    # Pasar el docente_id en el contexto
    context = {
        'docente_id': docente_id
    }
    return render(request, 'consult.html', context)

@login_required
def modify_privacy(request):
    return render(request, 'modify-privacy.html')

@login_required
def create(request):
    if request.method == "POST":  # Corregido a comillas simples
        user = request.user
        docente = user.docente
        
        # Crear el CV asociado al docente
        nuevo_cv = CV.objects.create(docente=docente, fecha_creacion=timezone.now(), estado=1)
        
        # Redirige a la página de actualización del CV
        return redirect('update')  # Asegúrate de tener esta URL en urls.py
        
    return render(request, 'create.html')

@login_required
def update(request):
    return render(request, 'update.html')

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ExperienciaLaboral

@login_required
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

@login_required
def remove_experience(request, experiencia_id):
    experiencia = get_object_or_404(ExperienciaLaboral, id=experiencia_id)

    experiencia.delete()

    return redirect('update') 

@login_required
def register_academic_background(request):
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

@login_required
def remove_academic_background(request, formacion_id):
    # Obtener la formación académica que se quiere eliminar
    formacion = get_object_or_404(FormacionAcademica, id=formacion_id)

    # Eliminar la formación académica
    formacion.delete()
    return redirect('update')  

@login_required
def register_academic_production(request):
    if request.method == "POST":
        titulo = request.POST.get('titulo') 
        autor = request.POST.get('autor')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        tipo_produccion = request.POST.get('tipo_produccion')
        institucion = request.POST.get('institucion')

        user = request.user
        cv = user.docente.cv_docente  

        print(f"CV: {cv}")

        nueva_produccion = ProduccionAcademica(
            cv=cv, 
            titulo=titulo,
            autor=autor,
            fecha_publicacion=fecha_publicacion,
            tipo_produccion=tipo_produccion,
            institucion=institucion,
        )

        nueva_produccion.save()

        messages.success(request, "Academic production registered successfully.")

        return redirect('update')  
    return render(request, 'update.html')

@login_required
def remove_academic_production(request, produccion_id):
    # Obtener la producción académica que se quiere eliminar
    produccion = get_object_or_404(ProduccionAcademica, id=produccion_id)
    produccion.delete()

    messages.success(request, "Producción académica eliminada correctamente.")

    return redirect('update')  # Cambia 'update' por la URL que desees


#wilson
def generate_curriculum(request, docente_id):
    # Crear el documento en formato Word para edición
    docente = get_object_or_404(Docente, id=docente_id)
    doc = Document()

    # Títulos y subtítulos
    doc.add_heading(f'Currículum de {docente.nombre} {docente.apellido}', level=1)

    # Información de contacto
    doc.add_heading("Información de Contacto", level=2)
    doc.add_paragraph(f"Cédula: {docente.cedula or 'N/A'}")
    doc.add_paragraph(f"Correo: {docente.correo or 'N/A'}")
    doc.add_paragraph(f"Teléfono: {docente.num_telefono or 'N/A'}")

    # Información profesional
    doc.add_heading("Información Profesional", level=2)
    doc.add_paragraph(f"Universidad: {docente.universidad or 'N/A'}")
    doc.add_paragraph(f"Facultad: {docente.facultad or 'N/A'}")
    doc.add_paragraph(f"Especialidad: {docente.especialidad or 'N/A'}")
    doc.add_paragraph(f"Categoría: {docente.categoria or 'N/A'}")

    # Detalles del contrato
    doc.add_heading("Detalles del Contrato", level=2)
    doc.add_paragraph(f"Tipo de Contrato: {docente.tipo_contrato or 'N/A'}")
    doc.add_paragraph(f"Estado: {docente.estado or 'N/A'}")
    doc.add_paragraph(f"Fecha de Contratación: {docente.fecha_contratacion.strftime('%d/%m/%Y') if docente.fecha_contratacion else 'N/A'}")

     # Guardar documento Word temporal
    # temp_word = BytesIO()
    # doc.save(temp_word)
    # temp_word.seek(0)

    # # Convertir el documento en PDF
    # response = HttpResponse(content_type='application/pdf')
    # response['Content-Disposition'] = f'attachment; filename="{docente.nombre}_{docente.apellido}_curriculum.pdf"'

    # # Crear el PDF con ReportLab
    # pdf_canvas = canvas.Canvas(response, pagesize=letter)
    # pdf_canvas.setFont("Helvetica", 12)

    # Convertir el documento en PDF y almacenarlo en memoria
    pdf_buffer = BytesIO()
    pdf_canvas = canvas.Canvas(pdf_buffer, pagesize=letter)
    pdf_canvas.setFont("Helvetica", 12)

    # Añadir contenido al PDF
    y_position = 750  # Posición vertical inicial
    pdf_canvas.drawString(100, y_position, f"Currículum de {docente.nombre} {docente.apellido}")
    y_position -= 30
    pdf_canvas.drawString(100, y_position, "Información de Contacto:")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Cédula: {docente.cedula or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Correo: {docente.correo or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Teléfono: {docente.num_telefono or 'N/A'}")
    y_position -= 40

    pdf_canvas.drawString(100, y_position, "Información Profesional:")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Universidad: {docente.universidad or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Facultad: {docente.facultad or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Especialidad: {docente.especialidad or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Categoría: {docente.categoria or 'N/A'}")
    y_position -= 40

    pdf_canvas.drawString(100, y_position, "Detalles del Contrato:")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Tipo de Contrato: {docente.tipo_contrato or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Estado: {docente.estado or 'N/A'}")
    y_position -= 20
    pdf_canvas.drawString(120, y_position, f"Fecha de Contratación: {docente.fecha_contratacion.strftime('%d/%m/%Y') if docente.fecha_contratacion else 'N/A'}")

    # Finalizar PDF
    pdf_canvas.save()
    pdf_buffer.seek(0)

    response = HttpResponse(pdf_buffer, content_type='application/pdf')
    return response
    


@login_required
def privacidad(request):
    
    return render(request, 'pages/privacidad.html')
# Create your views here.
