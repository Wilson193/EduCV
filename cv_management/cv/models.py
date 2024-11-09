from django.db import models
from docente.models import Docente

# Create your models here.
class ExperienciaLaboral(models.Model):
    lugar_trabajo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField(null=True, blank=True)  # Permitir que sea nulo
    descripcion = models.CharField(max_length=3000, null=True, blank=True)  # Permitir que sea nulo
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='experiencia_laboral')

class FormacionAcademica(models.Model):
    nivel = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    pais = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='formacion_academica')
    
class ProduccionAcademica(models.Model):
    tipo = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha_realizacion = models.DateField()
    descripcion = models.CharField(max_length=3000)
    cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='produccion_academica')
    
# class Publicacion(models.Model):
#     tipo = models.CharField(max_length=100)
#     titulo = models.CharField(max_length=100)
#     fecha_publicacion = models.DateField()
#     enlace = models.URLField()
#     descripcion = models.CharField(max_length=3000)
#     cv = models.ForeignKey('CV', on_delete=models.CASCADE, related_name='publicaciones')

class CV(models.Model):
    fecha_creacion = models.DateField()
    estado = models.IntegerField()
    docente = models.OneToOneField(Docente, on_delete=models.CASCADE, related_name="cv_docente")

    

    
