from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from control_usuarios.models import User
from control_usuarios.forms import Userform

def signup(request):
    if request.method == "POST":
        userform = Userform(request.POST)
        if userform.is_valid():
            data = userform.cleaned_data
            mail = data["mail"]
            usuario = data["usuario"]
            password = data["password"]
            user = User(mail=mail, usuario=usuario, password=password)
            user.save()
            url_success = reverse('Registro exitoso')
            return redirect(url_success)
        else:
            userform = Userform(initial=request.POST)
            http_response = render(
            request=request,
            template_name='control_usuarios/signup.html',
            context={'userform': userform}
            )
            return http_response
    else:
        userform = Userform()
        http_response = render(
            request=request,
            template_name='control_usuarios/signup.html',
            context={'userform': userform}
        )
        return http_response

def login(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/login.html',
        context=contexto,
    )
    return http_response

def tags(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/tags.html',
        context=contexto,
    )
    return http_response

def profile(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/profile.html',
        context=contexto,
    )
    return http_response

def users(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/users.html',
        context=contexto,
    )
    return http_response

def users_search(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        users = User.objects.filter(usuario__contains=busqueda)
        contexto = {
            "usuario": users,
        }
        http_response = render(
        request=request,
        template_name='control_usuarios/users.html',
        context=contexto,
        )
        return http_response

def signsucc(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/sign-succ.html',
        context=contexto,
    )
    return http_response