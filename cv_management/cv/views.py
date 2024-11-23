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
from .models import Docente
from django.http import JsonResponse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from .models import Docente


def index(request):
  return render(request ,'users.html')


def search(request):
    return render(request, 'search.html')


def search_teacher_main(request):
    query = request.GET.get('query', '')
    docentes = Docente.objects.filter(
        nombre__icontains=query
    )
    return render(request, 'all_teachers.html', {'docentes': docentes, 'query': query})


def search_teacher_ajax(request):
    query = request.GET.get('query', '')
    if query:
        # Buscamos por nombre, apellido y especialidad
        docentes = Docente.objects.filter(
            nombre__icontains=query
        ) | Docente.objects.filter(
            apellido__icontains=query
        ) | Docente.objects.filter(
            especialidad__icontains=query
        )
        
        # Creamos una lista de resultados para devolver
        results = [{
            'id': docente.id,
            'nombre': docente.nombre,
            'apellido': docente.apellido,
            'especialidad': docente.especialidad,
            'facultad': docente.facultad,
            'cargo': docente.cargo,
            'fecha_contratacion': docente.fecha_contratacion,
            'correo': docente.correo,
            'foto': docente.foto.url if docente.foto else None  # Usamos la URL de la imagen si existe
        } for docente in docentes]
        print(results)
    else:
        results = []
    
    return JsonResponse(results, safe=False)



def docentes_resultados(request):
    query = request.GET.get('query', '')
    docentes = Docente.objects.filter(
        nombre__icontains=query) | Docente.objects.filter(
        apellido__icontains=query) | Docente.objects.filter(
        facultad__icontains=query)
        
    total_docentes = Docente.objects.count()
    
    return render(request, 'teachers.html', {'docentes': docentes, 'query': query, 'total_docentes': total_docentes})
    
def list_teachers(request): 
    query = request.GET.get('query', '')
    results = Docente.objects.filter(name__icontains=query) # Ajusta el filtro según tu modelo 
    return render(request, 'teachers.html', {'query': query, 'results': results})

@login_required
def teachers(request):
  return render(request, 'teachers.html')

def all_teachers(request):
    docentes = Docente.objects.all()
    total_docentes = Docente.objects.count()
    return render(request, 'all_teachers.html', {'docentes': docentes, 'total_docentes': total_docentes})

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
def consult(request):
    return render(request, 'consult.html')


@login_required
def modify_privacy(request):
    return render(request, 'modify-privacy.html')

@login_required
def verify(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    experiencias_verificadas = all(experiencia.estado for experiencia in docente.cv_docente.experiencia_laboral.all())
    formaciones_verificadas = all(formacion.estado for formacion in docente.cv_docente.formacion_academica.all())
    producciones_verificadas = all(produccion.estado for produccion in docente.cv_docente.produccion_academica.all())
    competencias_verificadas = all(competencia.estado for competencia in docente.cv_docente.competencias.all())
    # Renderiza la plantilla con el docente en el contexto
    
    contexto = {
        'docente': docente,
        'experiencias_verificadas': experiencias_verificadas,
        'formaciones_verificadas': formaciones_verificadas,
        'producciones_verificadas': producciones_verificadas,
        'competencias_verificadas': competencias_verificadas,
    }
    
    return render(request, 'verify.html', contexto)


@login_required
def verify_personal_data(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)
    docente.estado = True
    docente.save()
    return render(request, 'verify.html', {'docente': docente})
    
@login_required
def verify_item(request, model_name, item_id, docente_id):
    # Diccionario de modelos
    model_mapping = {
        'docente': Docente,
        'experiencia': ExperienciaLaboral,
        'formacion': FormacionAcademica,
        'produccion': ProduccionAcademica,
        'competencia': Competencia,
    }
    
    # Obtener el modelo dinámicamente
    model = model_mapping.get(model_name)
    if not model:
        # Si el modelo no existe, redirige a una página de error
        return redirect('error_page')

    # Obtener el objeto y marcarlo como verificado
    item = get_object_or_404(model, id=item_id)
    item.estado = True  # Actualizar el estado a 'Verificado'
    item.save()
    
    # Redirigir a la página original o de detalles
    return redirect('verify', docente_id)

@login_required
def update(request):
    return render(request, 'update.html')



@login_required
def update_status(request, docente_id):
    # Obtén el docente correspondiente por su ID
    docente = get_object_or_404(Docente, id=docente_id)

    # Accede al objeto CV asociado al docente
    cv = docente.cv_docente  # Relación del docente con su CV

    # Si el formulario fue enviado
    if request.method == 'POST':
        # Cambiar el estado de activo a inactivo o viceversa según el botón presionado
        if 'activar' in request.POST:
            cv.estado = True  # Cambiar a 'Activo'
            cv.save()  # Guardar cambios en el CV
        elif 'desactivar' in request.POST:
            cv.estado = False  # Cambiar a 'Inactivo'
            cv.save()  # Guardar cambios en el CV

        # Redirige a la misma página o a la página deseada después de la acción
        return redirect('update_status', docente_id=docente.id)

    # Renderiza la plantilla con los datos del docente y su CV
    return render(request, 'verify.html', {'docente': docente})


@login_required
def update_social_links(request):
    user = request.user
    cv = user.docente.cv_docente  # Usando el related_name

    if request.method == "POST":
        linkedin = request.POST.get('linkedin')
        x = request.POST.get('x')
        github = request.POST.get('github')
        
        cv.linkedin = linkedin
        cv.x = x
        cv.github = github
        cv.save()
        
        messages.success(request, "Redes sociales guardadas correctamente.")
        return redirect('update')  # Redirige a una vista de confirmación o detalles del CV

    return render(request, 'update.html')


@login_required
def register_experience(request):
    """Función para registrar una nueva experiencia laboral"""
    if request.method == "POST":
        # Recoger los datos del formulario
        empresa = request.POST.get('empresa')
        cargo = request.POST.get('cargo')
        fecha_inicio = request.POST.get('fecha_inicio')
        fecha_fin = request.POST.get('fecha_fin')
        descripcion = request.POST.get('descripcion')
        
        # Obtener el archivo
        certificado = request.FILES.get('certificado')  # Usar request.FILES para manejar archivos

        # Obtener el usuario y el CV relacionado con el docente
        user = request.user
        cv = user.docente.cv_docente  # Usando el related_name

        print(f"el valor de cv: {cv}")
        
        # Crear la nueva experiencia laboral
        nueva_experiencia = ExperienciaLaboral(
            cv=cv,  # Asociar la experiencia con el CV
            lugar_trabajo=empresa,
            cargo=cargo,
            fecha_inicio=fecha_inicio,
            fecha_fin=fecha_fin,
            descripcion=descripcion,
            certificado=certificado,  # Aquí ya tienes el archivo cargado
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
         # Obtener el archivo
        certificado = request.FILES.get('certificado')  # Usar request.FILES para manejar archivos
        print(f"este es el certificado {certificado}")
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
            pais=pais,
            certificado=certificado,
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
        tipo = request.POST.get('tipo')
        titulo = request.POST.get('titulo')
        fecha_publicacion = request.POST.get('fecha_publicacion')
        descripcion = request.POST.get('descripcion')

        user = request.user
        cv = user.docente.cv_docente  

        print(f"CV: {cv}")

        nueva_produccion = ProduccionAcademica(
            cv=cv, 
            tipo=tipo,
            titulo=titulo,
            fecha_publicacion=fecha_publicacion,
            descripcion=descripcion
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


@login_required
def register_competence(request):
    if request.method == "POST":
        nombre = request.POST.get('nombre')
        nivel = request.POST.get('nivel')

        user = request.user
        cv = user.docente.cv_docente  

        print(f"CV: {cv}")

        nueva_competencias = Competencia(
            cv=cv, 
            nombre = nombre,
            nivel = nivel,
        )

        nueva_competencias.save()

        messages.success(request, "Competence registered successfully.")

        return redirect('update')  
    return render(request, 'update.html')  


@login_required
def remove_competence(request, competence_id):
    # Obtener la producción académica que se quiere eliminar
    competence = get_object_or_404(Competencia, id=competence_id)
    competence.delete()

    messages.success(request, "Producción académica eliminada correctamente.")

    return redirect('update')  # Cambia 'update' por la URL que desees


@login_required
def privacidad(request):
    return render(request, 'pages/privacidad.html')


@login_required
def get_document(request):
    if request.method == "POST":
        cv = request.user.cv
        document = request.FILES.get('get_certificate')
        if document:
            cv.documento = document
            cv.save()
            return redirect ('update')
        if request.POST.get('remove_document') == 'true':
            cv.documento.delete(save=True)
            return redirect('update')  # Redirige después de eliminar el documento

    # Si no es un POST o no se subió ningún archivo
    return HttpResponse("Método no permitido o no se ha subido un documento", status=400)


def generate_curriculum(request, docente_id):
    try:
        docente = get_object_or_404(Docente, id=docente_id)
    except Docente.DoesNotExist:
        # Manejo de error, como redirigir o devolver un mensaje adecuado
        return HttpResponse("Docente no encontrado", status=404)
    
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
    response['Content-Disposition'] = f'inline; filename="{docente.nombre}_{docente.apellido}_curriculum.pdf"'
    return response