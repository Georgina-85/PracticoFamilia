from django.db import models

# Create your models here.
class Familiares(models.Model):
    nombre = models.CharField(max_length=40, default = None)
    apellido = models.CharField(max_length=40, default = None)
    fechaDeNacimiento = models.DateField(default = None)
    documento = models.CharField(max_length=8, default = None)

