from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.views import LogoutView
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

from control_usuarios.models import Etiqueta, Avatar
from control_usuarios.forms import Userform, Tagform, UserUpdateForm, AvatarForm

#--------- Signup, Login, Logout y Perfil

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


def signsucc(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/sign-succ.html',
        context=contexto,
    )
    return http_response


def login_view(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            next_page = request.GET.get('next')
            if next_page:
                return redirect(next_page)
            else:
                return redirect('Home')
    return render(request, 'control_usuarios/login.html')    # GET
    
class CustomLogoutView(LogoutView):
   template_name = 'control_usuarios/logout.html'


@login_required
def profile(request, id):
    user = User.objects.get(id=id)
    inicial = {
        'first_name': user.first_name,
        'last_name': user.last_name,
        'username': user.username,
        'email': user.email,
    }
    formulario = Userform(initial=inicial, instance=user)
    context = {
        'formulario': formulario
    }
    return render(request, 'control_usuarios/profile.html', context)


@login_required
def edit_profile(request, id):
   user = User.objects.get(id=id)
   if request.method == "POST":
       formulario = UserUpdateForm(request.POST)

       if formulario.is_valid():
           data = formulario.cleaned_data
           user.first_name = data['first_name']
           user.last_name = data['last_name']
           user.save()
           url_exitosa = reverse('Perfil', args=[id])
           return redirect(url_exitosa)
   else:  # GET
       inicial = {
           'first_name': user.first_name,
           'last_name': user.last_name,
       }
       formulario = UserUpdateForm(initial=inicial)
   return render(
       request=request,
       template_name='control_usuarios/edit-profile.html',
       context={'formulario': formulario},
   )
    

@login_required
def edit_avatar(request, id):
    usuario = get_object_or_404(User, id=id)
    avatar, created = Avatar.objects.get_or_create(user=usuario)
    if request.method == "POST":
        formulario = AvatarForm(request.POST, request.FILES, instance=avatar)
        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('Perfil', args=[id])
            return redirect(url_exitosa)
    else:  # GET
        formulario = AvatarForm(instance=avatar)

    return render(
        request=request,
        template_name="control_usuarios/edit-avatar.html",
        context={'form': formulario, 'user': usuario},
    )



#--------- Etiquetas


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


#--------- Users

@login_required
def users(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='control_usuarios/users.html',
        context=contexto,
    )
    return http_response

@login_required
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
    
