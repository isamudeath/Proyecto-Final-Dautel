from django.urls import path
from control_usuarios import views

urlpatterns = [
    path('signup/', views.signup, name="Registrarse"),
    path('login/', views.login, name="Ingresar"),
    path('tags/', views.tags, name="Etiquetas"),
    path('profile/', views.profile, name="Perfil"),
    path('users/', views.users, name="Usuarios"),
    path('sign-succ/', views.signsucc, name="Registro exitoso"),
    path('user-search/', views.users_search, name="Busqueda"),
    path('add-tag/', views.add_tag, name="Agregar etiqueta"),
    path('tag-succ', views.tagsucc, name="Creacion exitosa"),
    path('tag-search/', views.tag_search, name="Busqueda Etiqueta"),
]