# Proyecto Final Coder House - Python
#### Comisión: 40440
#### Alumno: Emanuel Dautel

## Nombre del Proyecto
Web blog

## Versión
1.0

## Instrucciones instalar proyecto en local
+ Crea una carpeta contenedora madre
+ Abre la consola y ubicate en la carpeta madre
+ Crea y activa el ambiente virtual
+ Clona este proyecto en la carpeta madre
+ Entra en la carpeta que acabas de clonar
+ Para instalar las dependencias corre este comando:

```
pip install -r requirements.txt
```
---
## Descripción del Proyecto
Página Web estilo blog.

Cualquier visitante puede navegar por las secciones de la página web, se requerirá iniciar sesión para crear Posts o Etiquetas.

Los usuarios no logueados pueden relaizar las siguientes acciones:
- Ver el home
- Ver la sección Posts y buscar Posts
- Ver el detalle de cualquier Post
- Ver la sección Etiquetas y buscar Etiqeutas
- Ver la página "Acerca de Mi"

Los usuarios logueados pueden realizar las siguientes accciones:
- Todas las acciones que puede realizar un usuario no logueado
- Ver la sección Usuarios y buscar Usuarios en la DB por nombre de usuario, Nombre o Apellido
- Crear Posts
- Editar y Eliminar sus propios Posts
- Visualizar el autor de los Posts
- Crear Etiquetas
- Visualizar el autor de las Etiquetas
- Editar el perfil de Usuario
- Ver el perfil de otros usuarios

Los usuarios admin logueados pueden realizar las siguientes accciones:
- Todas las acciones que puede realizar un usuario logueado
- Editar y Eliminar cualquier Post
- Acceder al panel administrativo de Django

## Secciones y Funcionalidades

### Tab "Inicio"
+ Esta tab es el Home de la página

### Tab "Posts"
+ En esta sección podemos ver y crear Posts, estos pueden contener texto e imagenes
+ Se muestran también los últimos 4 Posts creados y se puede reazlizar una busqueda por título de post

### Tab "Usuarios"
+ Esta tab solo es visible para los usuarios logueados
+ Aquí podremos efectuar una búsqueda de usuarios en la DB por nombre de usuario, Nombre o Apellido

### Tab "Etiquetas"
+ En esta tab podemos iniciar el proceso de creado de una etiqueta o buscar una etiqueta en la DB
+ Haciendo click en "Crear" nos redireccionará al formulario de creación

### Sign-up / Login
+ El botón Sign-up nos llevara al formulario de registro, todos los campos son obligatorios
+ El botón Login nos llevara a la página de inicio de sesión
+ Una vez que el usuario ha iniciado sesión correctamente estos botones son reemplazados por un botón dropdown con las opciones "Perfil", "Panel administrativo" (si el user es un admin) y "Logout"

### Perfil
+ Aqui podemos visualizar la información del usuario
+ Si el perfil es el del usuario autenticado, el usuario podrá editar sus datos y avatar

### Logout
+ Permite cerrar sesión

## Video Demostración
https://youtu.be/WdPl6ze16cs

# Superusuario de pruebas
username: adminfinal
contraseña: pass40440

# Usuarios normales
username: v2user
contraseña: Super!123

username: user3
contraseña: tercero3