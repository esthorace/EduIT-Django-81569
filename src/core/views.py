from datetime import datetime
from random import randint

from django.contrib.auth.decorators import login_not_required  # type:ignore
from django.contrib.auth.views import LoginView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .forms import MyAuthenticationForm


@login_not_required
def index(request):
    ahora = datetime.now().year
    contexto = {"año": ahora}
    return render(request, "core/index.html", context=contexto)


def saludar(request):
    return HttpResponse("¡Hola Django!")


def saludar_con_etiqueta(request):
    return HttpResponse("<h1> Este es el título de la página </h1>")


def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre_completo = f"{apellido.upper()}, {nombre.capitalize()}"
    return HttpResponse(f"Hola {nombre_completo}!")


def tirar_dado(request):
    tiro_de_dado = randint(1, 6)

    if tiro_de_dado == 6:
        mensaje = f"Has tirado el 🎲 y has obtenido ¡{tiro_de_dado}! 🎉 Ganaste!!!"
    else:
        mensaje = f"Has tirado el 🎲 y has obtenido ¡{tiro_de_dado}! 🥶"
    datos = {
        "titulo": "Tiro de Dados",
        "mensaje": mensaje,
        "fecha": datetime.now().strftime("%H:%M:%S.%f"),
    }
    return render(request, "core/pages/dados.html", context=datos)


def ejercicio_1(request: HttpRequest) -> HttpResponse:
    nombre: str = input("Nombre: ")
    apellido: str = input("Apellido: ")
    return render(
        request,
        "core/pages/ejercicio-1.html",
        {
            "nombre": nombre,
            "apellido": apellido,
        },
    )


def notas(request: HttpRequest) -> HttpResponse:
    lista_notas: list[int] = [10, 7, 3, 4, 9, 10, 1]
    return render(request, "core/pages/notas.html", {"notas": lista_notas})


def ejercicio_2(request: HttpRequest):
    usuarios: list[dict] = [
        {
            "nombre": "juan",
            "email": "juan@example.com",
        },
        {
            "nombre": "santi",
            "email": "santi@santiago.com",
        },
        {
            "nombre": "cintia",
            "email": "cintia@cint.com",
        },
    ]
    return render(request, "core/pages/ejercicio-2.html", {"usuarios": usuarios})


def mi_json(request):
    usuarios: list[dict] = [
        {
            "nombre": "juan",
            "email": "juan@example.com",
        },
        {
            "nombre": "santi",
            "email": "santi@santiago.com",
        },
        {
            "nombre": "cintia",
            "email": "cintia@cint.com",
        },
    ]
    return JsonResponse(usuarios, safe=False)


class MyLoginView(LoginView):
    authentication_form = MyAuthenticationForm
    template_name = "core/pages/login.html"
    next_page = reverse_lazy("core:index")
