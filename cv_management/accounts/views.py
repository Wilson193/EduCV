from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import authenticate, login
from docente.models import Docente, PrivacidadDocente
  # Asegúrate de importar tu modelo
from coordinador_academico.models import  CoordinadorAcademico  # Asegúrate de importar tu modelo
from accounts.models import User
from django.contrib.auth.models import Group
from django.contrib.auth import logout
from django.db import transaction

def signup(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        email = request.POST.get('email')
        password = request.POST.get('password')
        rol = request.POST.get('rol')
        
        try:
            with transaction.atomic():
                # Crear instancia de Docente o Coordinador sin asociar el User aún
                if rol == 'Docente':
                    docente = Docente.objects.create(cedula=cedula, correo=email)
                elif rol == 'Coordinador':
                    coordinador = CoordinadorAcademico.objects.create(cedula=cedula, correo=email)

                # Crear el usuario asociado
                user = User.objects.create_user(email=email, password=password, rol=rol)
                
                # Asignar el grupo correspondiente
                if rol == 'Docente':
                    group = Group.objects.get(name='Docente')
                    user.groups.add(group)
                    docente.user = user
                    docente.save()  # Guardar la relación del usuario con el docente
                    
                     # Inicializar los valores de privacidad para el docente
                    privacidad_docente = PrivacidadDocente.objects.create(
                        docente=docente,
                        cedula_visible=True,  # La cédula será visible por defecto
                        num_telefono_visible=True,  # El número de teléfono será visible por defecto
                        correo_visible=True,  # El correo será visible por defecto
                        categoria_visible=True,  # La categoría será visible por defecto
                        tipo_contrato_visible=True,  # El tipo de contrato será visible por defecto
                        fecha_contratacion_visible=True  # La fecha de contratación será visible por defecto
                    )
                    privacidad_docente.save()
                    
                elif rol == 'Coordinador':
                    group = Group.objects.get(name='Coordinador')
                    user.groups.add(group)
                    coordinador.user = user
                    coordinador.save()  # Guardar la relación del usuario con el coordinador

            return render(request, 'signup.html')  # O redirigir a otra página

        except Exception as e:
            # Si ocurre algún error, puedes mostrar un mensaje de error en la página
            # También puedes usar mensajes de Django o logs para manejar errores
            print(f"Error al crear el usuario: {e}")

    return render(request, 'signup.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)   
                 
            if user.groups.filter(name='Docente').exists():
                return redirect('dashboard')
            elif user.groups.filter(name='Coordinador').exists():
                return redirect('dashboard')
        else:
            messages.error(request, 'Credenciales inválidas.')
            print(request, 'Credenciales inválidas.')

    return render(request, 'signin.html')

def signout(request):
    logout(request) 
    return render(request, 'signin.html')
