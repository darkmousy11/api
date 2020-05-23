from django.db import models

# Create your models here.


class Persona(models.Model):
    id = models.AutoField(primary_key = True)
    nombre = models.CharField('Nombre', max_length=200)
    apellido = models.CharField('Apellido', max_length=200)