from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from control_usuarios.models import Etiqueta
from control_usuarios.forms import Userform, Tagform

def signup(request):
    if request.method == "POST":
        userform = Userform(request.POST)
        if userform.is_valid():
            userform.save()
            url_success = reverse('Registro exitoso')
            return redirect(url_success)
        else:
            for field, errors in userform.errors.items():
                messages.error(request, f"{', '.join(errors)}")
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


def login_view(request):
    next_url = request.GET.get('next')
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            usuario = data.get('username')
            password = data.get('password')
            user = authenticate(username=usuario, password=password)
            # user puede ser un usuario o None
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_success = reverse('Home')
                return redirect(url_success)
    else:  # GET
        form = AuthenticationForm()
    return render(
            request=request,
            template_name='control_usuarios/login.html',
            context={'form': form},
    )
    
class CustomLogoutView(LogoutView):
   template_name = 'control_usuarios/logout.html'


def tags(request):
    contexto = {
        "tags": Etiqueta.objects.all(),
    }
    http_response = render(
        request=request,
        template_name='control_usuarios/tags.html',
        context=contexto,
    )
    return http_response

@login_required
def add_tag(request):
    if request.method == "POST":
        tagform = Tagform(request.POST)
        if tagform.is_valid():
            data = tagform.cleaned_data
            nombre = data["nombre"]
            autor = request.user
            tag = Etiqueta(nombre=nombre, autor=autor)
            tag.save()
            url_success = reverse('Creacion exitosa')
            return redirect(url_success)
        else:
            for field, errors in tagform.errors.items():
                messages.error(request, f"{', '.join(errors)}")
            tagform = Tagform(initial=request.POST)
            http_response = render(
            request=request,
            template_name='control_usuarios/addtag.html',
            context={'tagform': tagform}
            )
            return http_response
    else:
        tagform = Tagform()
        http_response = render(
            request=request,
            template_name='control_usuarios/addtag.html',
            context={'tagform': tagform}
        )
        return http_response


def tag_search(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        tags = Etiqueta.objects.filter(nombre__contains=busqueda)
        contexto = {
            "nombre": tags,
            "autor": tags,
        }
        http_response = render(
        request=request,
        template_name='control_usuarios/tags.html',
        context=contexto,
        )
        return http_response


def tagsucc(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/tag-succ.html',
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

@login_required
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
        users = User.objects.filter(username__contains=busqueda)
        contexto = {
            "username": users,
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