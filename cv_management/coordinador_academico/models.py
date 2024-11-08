from django.db import models
from docente.models import Persona
from accounts.models import User

class CoordinadorAcademico(Persona):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="coordinador_academico", null=True, blank=True)
    dependencia = models.CharField(max_length=100, null=True, blank=True)
    telefono_oficina = models.BigIntegerField(null=True, blank=True)
    oficina = models.CharField(max_length=100, null=True, blank=True)
