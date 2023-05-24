from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts, name="Posts"),
    path('create-post/', views.create_post, name="Crear Post"),
    path('post-succ/', views.post_succ, name="Post creado"),
    path('<int:id>/detail/', views.post_detail, name="detalle"),
]