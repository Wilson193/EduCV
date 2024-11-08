from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Docente
from django.shortcuts import get_object_or_404 #wilson
from django.http import HttpResponse #wilson
from docx import Document #wilson
from docx.oxml import OxmlElement#wilson
from docx.oxml.ns import qn #wilson
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from docx.shared import Pt

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

        return redirect('update')

    return render(request, 'update.html')  # La plantilla del formulario de actualización

def update_picture(request):
    if request.method == "POST":
        user = request.user
        print(f"el valor es:{user.docente.profile_picture}")
        # Verificamos si se ha subido una imagen
        photo = request.FILES.get('profile_picture')
        if photo:
            # Aquí debes obtener el objeto del docente actual para actualizar su foto de perfil
            docente = request.user.docente  # O el método que uses para obtener el docente
            docente.profile_picture = photo
            docente.save()
            return redirect('update_teacher')  # Redirige a una página de éxito o de actualización
        
        # Lógica para eliminar la imagen de perfil si se envía la solicitud para eliminar
        if request.POST.get('remove_picture') == 'true':
            docente = request.user.docente  # Cambia según cómo obtienes el docente actual
            docente.profile_picture.delete(save=True)
            return redirect('update_teacher')  # Redirige después de eliminar la imagen

    # Si no es un POST o no se subió ningún archivo, puedes redirigir o mostrar un mensaje
    return HttpResponse("Método no permitido o no se ha subido una imagen", status=400)

def update_teacher(request):
    docente = request.user.docente  # Obtén el objeto del docente vinculado al usuario actual
    return render(request, 'update.html', {'docente': docente})

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
    temp_word = BytesIO()
    doc.save(temp_word)
    temp_word.seek(0)

    # Convertir el documento en PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="{docente.nombre}_{docente.apellido}_curriculum.pdf"'

    # Crear el PDF con ReportLab
    pdf_canvas = canvas.Canvas(response, pagesize=letter)
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
    return response