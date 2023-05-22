from django.urls import path
from control_usuarios import views
from control_usuarios.views import CustomLogoutView

urlpatterns = [
    path('signup/', views.signup, name="Registrarse"),
    path('login/', views.login_view, name="Ingresar"),
    path('tags/', views.tags, name="Etiquetas"),
    path('profile/<int:id>/', views.profile, name="Perfil"),
    path('users/', views.users, name="Usuarios"),
    path('sign-succ/', views.signsucc, name="Registro exitoso"),
    path('user-search/', views.users_search, name="Busqueda"),
    path('add-tag/', views.add_tag, name="Agregar etiqueta"),
    path('tag-succ', views.tagsucc, name="Creacion exitosa"),
    path('tag-search/', views.tag_search, name="Busqueda Etiqueta"),
    path('logout/', CustomLogoutView.as_view(), name="Salir"),
    path('edit-profile/<int:id>/', views.edit_profile, name="editar_perfil"),
    path('edit-avatar/<int:id>/', views.edit_avatar, name="editar_avatar"),
    path('delete-avatar/<int:id>/', views.delete_avatar, name="borrar_avatar"),
]