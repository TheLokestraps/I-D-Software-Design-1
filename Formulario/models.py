from django.db import models
from django.db.models.fields import CharField

class Formulario (models.Model):
    nombreCompleto = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 40)
    indicativo =  models.IntegerField()
    telefono =  models.IntegerField()
    docIdentidad = models.IntegerField()
    imagen = models.ImageField(upload_to="productos")
