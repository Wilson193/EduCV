from django.db import models
from docente.models import Persona

class CoordinadorAcademico(Persona):
    dependencia = models.CharField(max_length=100)
    telefono_oficina = models.BigIntegerField()
    oficina = models.CharField(max_length=100)
