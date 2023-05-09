from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

from posts.models import Post
from posts.forms import Postform

def posts(request):
    contexto = {}
    http_response = render(
        request=request,
        template_name='posts/posts.html',
        context=contexto,
    )
    return http_response