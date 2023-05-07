from django.urls import path
from control_usuarios import views

urlpatterns = [
    path('signup/', views.signup, name="Registrarse"),
    path('login/', views.login, name="Ingresar"),
    path('tags/', views.tags, name="Etiquetas"),
    path('profile/', views.profile, name="Perfil"),
    path('users/', views.users, name="Usuarios"),
]