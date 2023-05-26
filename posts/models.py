from django.db import models
from django.core.validators import validate_slug, MinLengthValidator
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):

    titulo = models.CharField(max_length=256, validators=[MinLengthValidator(1)],)
    contenido = models.TextField(max_length=4000)
    imagen = models.ImageField(upload_to='post_images', null=True, blank=True, height_field=None, width_field=None, max_length=None)
    etiqueta = models.CharField(max_length=10, validators=[validate_slug])
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    fecha_mod = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.titulo}\nAutor: {self.autor}\nPublicado en: {self.fecha}"
    
    def get_absolute_url(self):
        return reverse('detalle', args=[str(self.id)])
