from django.db import models
from docente.models import Persona
from accounts.models import User

class CoordinadorAcademico(Persona):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="coordinador_academico")
    dependencia = models.CharField(max_length=100)
    telefono_oficina = models.BigIntegerField()
    oficina = models.CharField(max_length=100)
