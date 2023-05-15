from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import validate_slug, MinLengthValidator


class User(models.Model):

    nombre = models.CharField(max_length=40, validators=[validate_slug])
    apellido = models.CharField(max_length=40, validators=[validate_slug])
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=15, validators=[MinLengthValidator(8)])

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=10, unique=True, validators=[validate_slug])
    autor = models.CharField(max_length=20, default="unsigned_user", editable=False)

    def __str__(self):
        return f"{self.nombre}"