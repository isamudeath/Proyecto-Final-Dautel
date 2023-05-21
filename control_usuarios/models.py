from django.db import models
from django.core.validators import validate_slug
from django.contrib.auth.models import User

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=10, unique=True, validators=[validate_slug])
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.nombre}"