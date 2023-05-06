from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, MinLengthValidator


class user(models.Model):

    nombre = models.CharField(max_length=40, validators=[validate_slug])
    apellido = models.CharField(max_length=40, validators=[validate_slug])
    mail = models.EmailField()
    usuario = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=15, validators=[MinLengthValidator(8)])

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class etiqueta(models.Model):
    nombre = models.CharField(max_length=10, validators=[validate_slug])
    # autor = usuario

    def __str__(self):
        return f"{self.nombre}"