from django.db import models

from .colaborador import Usuario

class Alumno(models.Model):
    store = models.ForeignKey(Usuario)
    
