from django.db import models

# Create your models here.

class Alumno(models.Model): # Se crea un modelo.
    nombre = models.CharField(max_length=20)
    curso = models.CharField(max_length=20)