from django import forms
from django.core.validators import validate_slug, MinLengthValidator

class Userform(forms.Form):

    mail = forms.EmailField(required=True)
    usuario = forms.CharField(max_length=20, validators=[MinLengthValidator(4)], required=True)
    password = forms.CharField(max_length=15, validators=[MinLengthValidator(8)], widget=forms.PasswordInput(), required=True)