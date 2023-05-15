from django import forms
from django.core.validators import validate_slug, MinLengthValidator
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms.fields import EmailField
from django.forms.forms import Form

class Userform(UserCreationForm):

    email = forms.EmailField(label='email', required=True)
    username = forms.CharField(min_length=5, max_length=20, required=True)
    password1 = forms.CharField(label='password', widget=forms.PasswordInput(), max_length=15, min_length=8, required=True)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput(), max_length=15, min_length=8, required=True)

    def clean_username(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():
            raise ValidationError("El usuario ya existe")  
        return username

    def clean_email(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError("El mail ya se encuentra registrado")  
        return email
    
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  

        if password1 and password2 and password1 != password2:  
            raise ValidationError("Las contraseñas no coinciden")
        return password2

    def save(self, commit = True):  
        user = User.objects.create_user(
            username=self.cleaned_data['username'],  
            email=self.cleaned_data['email'],  
            password=self.cleaned_data['password1']  
        ) 
        return user

class Tagform(forms.Form):

    nombre = forms.CharField(max_length=10, validators=[MinLengthValidator(1)], required=True)