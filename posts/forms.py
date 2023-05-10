from django import forms
from django.core.validators import validate_slug, MinLengthValidator

class Postform(forms.Form):

    titulo = forms.CharField(max_length=256, validators=[MinLengthValidator(1)], required=True)
    contenido = forms.CharField(widget=forms.Textarea())
    #imagenes = forms.ImageField()
