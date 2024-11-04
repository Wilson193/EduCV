from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from docente.models import Docente  # Asegúrate de importar tu modelo

def signin(request):
        docente = Docente(
        cedula=123,
        nombre='nombre',
        apellido='apellido',
        num_telefono=1234,
        universidad='universidad',
        cargo='cargo',
        correo='correo',
        clave='2312',  # Si decides mantener este campo, considera encriptarlo.
        facultad='facultad',
        categoria='categoria',
        especialidad='especialidad',
        tipo_contrato='tipo_contrato',
        estado='estado',
        fecha_contratacion='2000-09-23'
        )
        docente.save()  # Guarda el nuevo docente en la base de datos
        return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

