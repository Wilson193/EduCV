from django.db import models

# Create your models here.
class ExperienciaLaboral(models.Model):
    lugar_trabajo = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    descripcionn = models.CharField(max_length=3000)
    
class FormaciónAcademica(models.Model):
    nivel = models.CharField(max_length=100)
    institucion = models.CharField(max_length=100)
    titulo = models.CharField(max_length=100)
    fecha_obtencion = models.DateField()
    
class ProduccionAcademica(models.Model):
     pass
  
    
class CV(models.Model):
    fecha_creacion = models.DateField()
    estado = models.IntegerField()
    
