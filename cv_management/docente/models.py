from django.db import models
from accounts.models import User

class Persona(models.Model):
    cedula = models.BigIntegerField(unique=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    apellido = models.CharField(max_length=100, null=True, blank=True)
    num_telefono = models.BigIntegerField(null=True, blank=True)
    universidad = models.CharField(max_length=100, null=True, blank=True)
    cargo = models.CharField(max_length=100, null=True, blank=True)
    correo = models.EmailField(unique=True)
    clave = models.CharField(max_length=20, null=True, blank=True)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    
    class Meta:
        abstract = True 

class Docente(Persona):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="docente", null=True, blank=True)
    facultad = models.CharField(max_length=100, null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True, blank=True)
    especialidad = models.CharField(max_length=100, null=True, blank=True)
    tipo_contrato = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=50, null=True, blank=True)
    fecha_contratacion = models.DateField(null=True, blank=True)
    estado = models.BooleanField(default=False)  # Comienza como False por defecto
    cv = models.OneToOneField('cv.CV', on_delete=models.CASCADE, null=True, blank=True, related_name='docente_cv')

class PrivacidadDocente(models.Model):
    docente = models.OneToOneField(Docente, on_delete=models.CASCADE)
    cedula_visible = models.BooleanField(default=True)
    num_telefono_visible = models.BooleanField(default=True)
    correo_visible = models.BooleanField(default=True)
    categoria_visible = models.BooleanField(default=True)
    tipo_contrato_visible = models.BooleanField(default=True)
    fecha_contratacion_visible = models.BooleanField(default=True)

    

