from django.urls import path
from control_usuarios import views

urlpatterns = [
    path('signup/', views.signup, name="Registrase"),
    path('login/', views.login, name="Ingresar"),
    path('tags/', views.tags, name="Etiquetas"),
]