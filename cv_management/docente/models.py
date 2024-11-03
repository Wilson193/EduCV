from django.db import models

# Create your models here.
class Persona(models.Model):
    cedula = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    num_telefono = models.BigIntegerField()
    universidad = models.CharField(max_length=100)
    cargo = models.CharField(max_length=100)
    
    class Meta:
        abstract = True

class Docente(Persona):
    facultad = models.CharField(max_length=100)
    categoria = models.CharField(max_length=50)
    especialidad = models.CharField(max_length=100)
    tipo_contrato = models.CharField(max_length=50)
    estado = models.CharField(max_length=50)
    fecha_contratacion = models.DateField()