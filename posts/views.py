from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from posts.models import Post
from posts.forms import Postform

def posts(request):
    num_posts = 4  # Número de últimos objetos a mostrar
    posts = Post.objects.order_by('-fecha')[:num_posts]
    contexto = {'posts': posts}
    return render(
        request, 
        'posts/posts.html', 
        contexto
        )


@login_required
def create_post(request):
    if request.method == "POST":
        postform = Postform(request.POST)
        if postform.is_valid():
            data = postform.cleaned_data
            titulo = data["titulo"]
            contenido = data["contenido"]
            autor = request.user
            post = Post(titulo=titulo, contenido=contenido,  autor=autor)
            post.save()
            url_success = reverse('Post creado')
            return redirect(url_success)
        else:
            for field, errors in postform.errors.items():
                messages.error(request, f"{', '.join(errors)}")
            postform = Postform(initial=request.POST)
            http_response = render(
            request=request,
            template_name='posts/create-post.html',
            context={'postform': postform}
            )
            return http_response
    else:
        postform = Postform()
        http_response = render(
            request=request,
            template_name='posts/create-post.html',
            context={'postform': postform}
        )
        return http_response
    #
    if request.method == "POST":
        postform = Postform(request.POST)
        if postform.is_valid():
            data = postform.cleaned_data
            print(data)
            titulo = data["titulo"]
            contenido = data["contenido"]
            post = Post(titulo=titulo, contenido=contenido)
            post.save()
            url_success = reverse('Post creado')
            return redirect(url_success)
        else:
            postform = Postform(initial=request.POST)
            http_response = render(
            request=request,
            template_name='posts/create-post.html',
            context={'postform': postform}
            )
            return http_response
    else:
        postform = Postform()
        http_response = render(
            request=request,
            template_name='posts/create-post.html',
            context={'postform': postform}
        )
        return http_response

def post_succ(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='posts/post-succ.html',
        context=contexto,
    )
    return http_response