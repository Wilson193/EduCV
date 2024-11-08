from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Docente
from django.shortcuts import get_object_or_404 #wilson
from django.http import HttpResponse #wilson
from docx import Document #wilson
from docx.oxml import OxmlElement#wilson
from docx.oxml.ns import qn #wilson
import os #wilson
import pypandoc #wilson
import tempfile #wilson
from django.http import HttpResponse

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

#wilson
def generate_curriculum(request, docente_id):
    docente = get_object_or_404(Docente, id=docente_id)

    # Asegúrate de que nombre y apellido no sean None
    nombre = docente.nombre or "SinNombre"
    apellido = docente.apellido or "SinApellido"

    doc = Document()
    doc.add_heading(f'Currículum de {docente.nombre} {docente.apellido}', level=1)

    # Información de contacto
    doc.add_heading("Información de Contacto", level=2)
    contact_info = doc.add_paragraph()
    contact_info.add_run("Cédula: ").bold = True
    contact_info.add_run(str(docente.cedula) if docente.cedula else "N/A")
    contact_info.add_run("\nCorreo: ").bold = True
    contact_info.add_run(docente.correo)
    contact_info.add_run("\nTeléfono: ").bold = True
    contact_info.add_run(str(docente.num_telefono) if docente.num_telefono else "N/A")

    # Información profesional
    doc.add_heading("Información Profesional", level=2)
    prof_info = doc.add_paragraph()
    prof_info.add_run("Universidad: ").bold = True
    prof_info.add_run(docente.universidad or "N/A")
    prof_info.add_run("\nFacultad: ").bold = True
    prof_info.add_run(docente.facultad or "N/A")
    prof_info.add_run("\nEspecialidad: ").bold = True
    prof_info.add_run(docente.especialidad or "N/A")
    prof_info.add_run("\nCategoría: ").bold = True
    prof_info.add_run(docente.categoria or "N/A")

    # Detalles del contrato
    doc.add_heading("Detalles del Contrato", level=2)
    contract_info = doc.add_paragraph()
    contract_info.add_run("Tipo de Contrato: ").bold = True
    contract_info.add_run(docente.tipo_contrato or "N/A")
    contract_info.add_run("\nEstado: ").bold = True
    contract_info.add_run(docente.estado or "N/A")
    contract_info.add_run("\nFecha de Contratación: ").bold = True
    contract_info.add_run(docente.fecha_contratacion.strftime("%d/%m/%Y") if docente.fecha_contratacion else "N/A")

    # Añade líneas divisorias debajo de cada subtítulo
    for paragraph in doc.paragraphs:
        if paragraph.style.name == 'Heading 2':
            # Verifica o crea el elemento 'pPr' en el párrafo
            p_pr = paragraph._element.get_or_add_pPr()
            
            # Agrega el borde inferior
            border = OxmlElement('w:pBdr')
            bottom_border = OxmlElement('w:bottom')
            bottom_border.set(qn('w:val'), 'single')
            bottom_border.set(qn('w:sz'), '6')
            bottom_border.set(qn('w:space'), '1')
            bottom_border.set(qn('w:color'), '000000')
            
            # Añade el borde al elemento pPr
            border.append(bottom_border)
            p_pr.append(border)

            # Crear archivos temporales de forma manual para evitar su eliminación prematura
            temp_dir = tempfile.mkdtemp()  # Crea un directorio temporal
            word_path = os.path.join(temp_dir, f"{nombre}_{apellido}.docx")
            pdf_path = os.path.join(temp_dir, f"{nombre}_{apellido}.pdf")

            try:
                # Guardar el archivo Word
                doc.save(word_path)

                # Convertir el documento Word a PDF
                pypandoc.convert_file(word_path, 'pdf', outputfile=pdf_path)

                # Leer el archivo PDF y devolverlo como respuesta
                with open(pdf_path, 'rb') as pdf_file:
                    response = HttpResponse(pdf_file.read(), content_type='application/pdf')
                    response['Content-Disposition'] = f'attachment; filename="{nombre}_{apellido}.pdf"'

            finally:
                # Limpieza manual de los archivos y directorio temporal
                if os.path.exists(word_path):
                    os.remove(word_path)
                if os.path.exists(pdf_path):
                    os.remove(pdf_path)
                if os.path.exists(temp_dir):
                    os.rmdir(temp_dir)

    return response