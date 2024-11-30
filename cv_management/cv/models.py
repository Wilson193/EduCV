from django.db import models
from docente.models import Docente
from coordinador_academico.models import CoordinadorAcademico

class PrivacidadCV():
    cv = models.OneToOneField('CV', on_delete=models.CASCADE, related_name="privacidad")
    linkedin_visible = models.BooleanField(default=True)
    x_visible = models.BooleanField(default=True)
    github_visible = models.BooleanField(default=True)
    gmail_enviable = models.BooleanField(default=True)
    outlook_enviable = models.BooleanField(default=True)

class Observacion(models.Model):
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='observaciones')
    autor = models.ForeignKey(CoordinadorAcademico, on_delete=models.CASCADE)  # Relación actualizada
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    leido = models.BooleanField(default=False)  # Para que el docente marque como leído

class Competencia(models.Model):
    nombre = models.CharField(max_length=100)
    nivel = models.CharField(max_length=100)
    estado = models.BooleanField(default=False)  # Comienza como False por defecto
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='competencias') 
    
class ExperienciaLaboral(models.Model):
    lugar_trabajo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)  # Permitir que sea nulo
    descripcion = models.CharField(max_length=3000, null=True, blank=True)  # Permitir que sea nulo
    estado = models.BooleanField(default=False)  # Comienza como False por defecto
    certificado = models.FileField(upload_to='certificados/', null=True, blank=True)  # Permitir que sea nulo
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='experiencia_laboral')

class FormacionAcademica(models.Model):
    nivel = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    estado = models.BooleanField(default=False)  # Comienza como False por defecto
    certificado = models.FileField(upload_to='certificados/', null=True, blank=True)  # Permitir que sea nulo
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='formacion_academica')
    
class ProduccionAcademica(models.Model):
    tipo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha_publicacion = models.DateField()
    descripcion = models.CharField(max_length=3000)
    estado = models.BooleanField(default=False)  # Comienza como False por defecto
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='produccion_academica')

class CV(models.Model):
    fecha_creacion = models.DateField()
    linkedin = models.URLField(max_length=200, null=True, blank=True)
    github = models.URLField(max_length=200, null=True, blank=True)
    x = models.URLField(max_length=200, null=True, blank=True)
    estado = models.BooleanField(default=False)  # Comienza como False por defecto
    
    # Definición de estados de verificación
    ESTADOS_VERIFICACION = (
        (0, 'Pendiente'),
        (1, 'Verificado'),
        (2, 'Validado'),
    )
    
    estado_verificacion = models.IntegerField(choices=ESTADOS_VERIFICACION, default=0)
    docente = models.OneToOneField(Docente, on_delete=models.CASCADE, related_name="cv_docente")