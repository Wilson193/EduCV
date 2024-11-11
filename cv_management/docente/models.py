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
    foto = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    cv = models.OneToOneField('cv.CV', on_delete=models.CASCADE, null=True, blank=True, related_name='docente_cv')
