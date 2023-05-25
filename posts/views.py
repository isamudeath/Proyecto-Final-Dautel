from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone

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


def post_detail(request, id):
    post = Post.objects.get(id=id)
    context = {
        'post': post
    }
    return render(request, 'posts/detail.html', context)


@login_required
def create_post(request):
    if request.method == "POST":
        postform = Postform(request.POST)
        if postform.is_valid():
            data = postform.cleaned_data
            titulo = data["titulo"]
            contenido = data["contenido"]
            autor = request.user
            post = Post(titulo=titulo, contenido=contenido, autor=autor)
            post.save()
            url_success = reverse('detalle', args=[post.id])
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
 

@login_required
def edit_post(request, id):
    post = Post.objects.get(id=id)
    detalle_url = post.get_absolute_url()
    if request.method == "POST":
        postform = Postform(request.POST, initial={'titulo': post.titulo, 'contenido': post.contenido})

        if postform.is_valid():
            data = postform.cleaned_data
            post.titulo = data["titulo"]
            post.contenido = data["contenido"]
            post.fecha_mod = timezone.now()
            post.save()
            url_exitosa = reverse('detalle', args=[post.id])
            return redirect(url_exitosa)
    else:  # GET
        inicial = {
            'titulo': post.titulo,
            'contenido': post.contenido,
        }
        postform = Postform(initial=inicial)
    return render(
        request=request,
        template_name='posts/edit-post.html',
        context={'postform': postform, 'detalle_url': detalle_url, 'post': post},
    )


@login_required
def delete_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        post.delete()
        return redirect('post_borrado')
    else:
        return render(request, 'posts/delete-post.html', {'post': post})


def post_deleted(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='posts/post-deleted.html',
        context=contexto,
    )
    return http_response


def post_search(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        posts = Post.objects.filter(titulo__contains=busqueda)
        contexto = {
            'posts': posts
        }
    return render(
        request, 
        'posts/posts.html', 
        contexto
        )