from django.urls import path
from posts import views

urlpatterns = [
    path('', views.posts, name="Posts"),
    path('create-post/', views.create_post, name="Crear Post"),
    path('<int:id>/detail/', views.post_detail, name="detalle"),
    path('<int:id>/edit/', views.edit_post, name="editar_post"),
    path('delete-post/<int:id>/', views.delete_post, name="borrar_post"),
    path('post-deleted/', views.post_deleted, name="post_borrado"),
    path('post-search/', views.post_search, name="Busqueda Post"),
]