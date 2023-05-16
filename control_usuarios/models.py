from django.db import models
from django.core.validators import validate_slug

class Etiqueta(models.Model):
    nombre = models.CharField(max_length=10, unique=True, validators=[validate_slug])
    autor = models.CharField(max_length=20, default="unsigned_user", editable=False)

    def __str__(self):
        return f"{self.nombre}"