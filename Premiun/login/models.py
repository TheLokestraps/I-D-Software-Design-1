from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre     = models.CharField(max_length=30)
    apellido   = models.CharField(max_length=30)
    direccion  = models.CharField(max_length=50)
    email      = models.EmailField()
    estrato    = models.IntegerField()
    cel        = models.CharField(max_length=10)
    password   = models.CharField(max_length=50)
