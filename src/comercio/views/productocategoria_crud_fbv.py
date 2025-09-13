from django.contrib.auth.decorators import login_not_required  # type:ignore
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from ..forms import ProductoCategoriaForm
from ..models import ProductoCategoria


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "comercio/index.html")


# READ (list)
def productocategoria_list(request: HttpRequest) -> HttpResponse:
    buscar = request.GET.get("consulta")
    if buscar:
        lista_de_registros = ProductoCategoria.objects.filter(nombre__icontains=buscar)
    else:
        lista_de_registros = ProductoCategoria.objects.all()
    contexto = {"productocategoria": lista_de_registros}
    return render(request, "comercio/productocategoria_list.html", contexto)


# CREATE
def productocategoria_create(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ProductoCategoriaForm()

    if request.method == "POST":
        form = ProductoCategoriaForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            form.save()
            return redirect("comercio:productocategoria_list")

    return render(request, "comercio/productocategoria_form.html", {"form": form})


# READ (DETAIL)
def productocategoria_detail(request: HttpRequest, pk: int):
    registro = ProductoCategoria.objects.get(id=pk)
    return render(
        request, "comercio/productocategoria_detail.html", {"object": registro}
    )


# UPDATE
def productocategoria_update(request: HttpRequest, pk: int) -> HttpResponse:
    registro = ProductoCategoria.objects.get(id=pk)
    if request.method == "GET":
        form = ProductoCategoriaForm(instance=registro)

    if request.method == "POST":
        form = ProductoCategoriaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect("comercio:productocategoria_list")

    return render(request, "comercio/productocategoria_form.html", {"form": form})


# DELETE
def productocategoria_delete(request: HttpRequest, pk: int) -> HttpResponse:
    registro = ProductoCategoria.objects.get(id=pk)
    if request.method == "POST":
        registro.delete()
        return redirect("comercio:productocategoria_list")
    return render(
        request, "comercio/productocategoria_confirm_delete.html", {"object": registro}
    )
