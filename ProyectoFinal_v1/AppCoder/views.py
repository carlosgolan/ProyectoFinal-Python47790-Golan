from datetime import date

from django.shortcuts import redirect, render

from datetime import datetime
from . import models
from .models import Curso, Profesor

from .forms import CursoFormulario, CursoBuscarFormulario, ProfesorFormulario

from django.contrib.auth.decorators import login_required


def inicio_view(request):
    return render(request, "AppCoder/inicio.html")

def about_view(request):
    return render(request, "AppCoder/about.html")


def cursos_buscar_view(request):
    if request.method == "GET":
        form = CursoBuscarFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_busqueda.html",
            context={"form": form}
        )
    else:
        formulario = CursoBuscarFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cursos_filtrados = []
            for curso in Curso.objects.filter(curso=informacion["curso"]):
                cursos_filtrados.append(curso)

            contexto = {"cursos": cursos_filtrados}
            return render(request, "AppCoder/cursos_list.html", contexto)


def cursos_todos_view(request):
    todos_los_cursos = []
    for curso in Curso.objects.all():
        todos_los_cursos.append(curso)

    contexto = {"cursos": todos_los_cursos}
    return render(request, "AppCoder/cursos_list.html", contexto)

@login_required
def cursos_view(request):
    if request.method == "GET":
        print("+" * 90) #  Imprimimos esto para ver por consola
        print("+" * 90) #  Imprimimos esto para ver por consola
        form = CursoFormulario()
        return render(
            request,
            "AppCoder/curso_formulario_avanzado.html",
            context={"form": form}
        )
    else:
        formulario = CursoFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            modelo = Curso(curso=informacion["curso"], camada=informacion["camada"])
            modelo.save()

        return redirect("AppCoder:inicio")


def profesores_view(xx):
    nombre = "Mariano Manuel"
    apellido = "Barracovich"
    ahora = datetime.now()
    diccionario = {
        'nombre': nombre,
        'apellido': apellido,
        "nacionalidad": "argentino",
        "hora": ahora,
        "ciudades_preferidas": ["Buenos Aires", "Lima", "San Pablo", "Trieste"]
    }  # Para enviar al contexto
    return render(xx, "AppCoder/padre.html", diccionario)


def lista_profesores(req):

    profesores = Profesor.objects.all()

    return render(req, "AppCoder/leerProfesores.html", {"lista_profesores": profesores})

@login_required
def crea_profesor(req):

    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data
            profesor = Profesor(nombre=data["nombre"], email=data["email"])
            profesor.save()

            return redirect("AppCoder:crea-profesor")
        
        return render(req, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

    else:

        miFormulario = ProfesorFormulario()

        return render(req, "AppCoder/profesorFormulario.html", {"miFormulario": miFormulario})

@login_required
def eliminar_profesor(req, id):

    if req.method == 'POST':

        profesor = Profesor.objects.get(id=id)
        profesor.delete()

        profesores = Profesor.objects.all()

        return render(req, "AppCoder/leerProfesores.html", {"lista_profesores": profesores})

@login_required
def editar_profesor(req, id):

    profesor = Profesor.objects.get(id=id)

    if req.method == 'POST':
        miFormulario = ProfesorFormulario(req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            profesor.nombre = data["nombre"]
            profesor.email = data["email"]
            profesor.save()

            return redirect("AppCoder:lista-profesores")
        
        return render(req, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario})

    else:

        miFormulario = ProfesorFormulario(initial={
            "nombre": profesor.nombre,
            "email": profesor.email
        })

        return render(req, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "id": profesor.id})  
    

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

def login_view(request):

    if request.user.is_authenticated:
        return render(
            request,
            "AppCoder/inicio.html",
            {"mensaje": f"Ya estás autenticado: {request.user.username}"}
        )

    if request.method == "GET":
        return render(
            request,
            "AppCoder/login.html",
            {"form": AuthenticationForm()}
        )
    else:
        formulario = AuthenticationForm(request, data=request.POST)

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            password = informacion["password"]

            modelo = authenticate(username=usuario, password=password)
            login(request, modelo)

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Bienvenido {modelo.username}"}
            )
        else:
            return render(
                request,
                "AppCoder/login.html",
                {"form": formulario}
            )


from django.contrib.auth import logout
def logout_view(request):
    logout(request)
    return render(request, "AppCoder/logout.html")
    #pass


from .forms import UserCreationFormulario, UserEditionFormulario
from django.contrib.auth.views import PasswordChangeView


def registro_view(request):

    if request.method == "GET":
        return render(
            request,
            "AppCoder/registro.html",
            {"form": UserCreationFormulario()}
        )
    else:
        formulario = UserCreationFormulario(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario = informacion["username"]
            formulario.save()

            return render(
                request,
                "AppCoder/inicio.html",
                {"mensaje": f"Usuario creado: {usuario}"}
            )
        else:
            return render(
                request,
                "AppCoder/registro.html",
                {"form": formulario}
            )