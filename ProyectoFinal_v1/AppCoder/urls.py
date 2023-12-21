from django.urls import path
#from django.contrib.auth.views import LogoutView

from AppCoder.views import (
    cursos_view, 
    cursos_buscar_view, 
    cursos_todos_view, 
    inicio_view, 
    about_view, 
    lista_profesores, 
    crea_profesor, 
    eliminar_profesor, 
    editar_profesor, 
    registro_view, 
    login_view,
    logout_view,
    )

app_name = "AppCoder"

urlpatterns = [
    path("cursos/", cursos_view, name="cursos"),
    path("cursos/todos", cursos_todos_view, name="cursos-todos"),
    path("cursos/buscar", cursos_buscar_view, name="cursos-buscar"),
    path("inicio/", inicio_view, name="inicio"),
    path("about/", about_view, name="about"),
    path("lista-profesores/", lista_profesores, name="lista-profesores"),
    path("crea-profesor/", crea_profesor, name="crea-profesor"),
    path("elimina-profesor/<int:id>", eliminar_profesor, name="elimina-profesor"),
    path("editar-profesor/<int:id>", editar_profesor, name="editar-profesor"),
    path("registro", registro_view, name="registro"),
    path("login", login_view, name="login"),
    #path("logout", LogoutView.as_view(template_name="AppCoder/logout.html"), name="logout"),
    path("logout", logout_view, name="logout"), 
]
