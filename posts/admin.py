from django.contrib import admin
from control_usuarios.models import Avatar, Etiqueta
from posts.models import Post


admin.site.register(Avatar)
admin.site.register(Post)
admin.site.register(Etiqueta)
