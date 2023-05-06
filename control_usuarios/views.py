from django.shortcuts import render
from django.http import HttpResponse


def signup(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/signup.html',
        context=contexto,
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