from typing import Any

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from ..forms import ProductoCategoriaForm
from ..models import ProductoCategoria


class Index(TemplateView):
    template_name = "comercio/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Mi Negocio"
        return context


class ProductoCatergoriaList(ListView):
    model = ProductoCategoria
    template_name = "comercio/productocategoria/productocategoria_list.html"
    # queryset = ProductoCategoria.objects.all()
    # context_object_name = "object_list"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        buscar = self.request.GET.get("consulta")
        if buscar:
            queryset = ProductoCategoria.objects.filter(nombre__icontains=buscar)
        else:
            queryset = ProductoCategoria.objects.all()
        return queryset


class ProductoCategoriaCreate(CreateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    template_name = "comercio/productocategoria/productocategoria_form.html"
    success_url = reverse_lazy("comercio:productocategoria_list")


class ProductoCategoriaDetail(DetailView):
    model = ProductoCategoria
    template_name = "comercio/productocategoria/productocategoria_detail.html"


class ProductoCategoriaUpdate(UpdateView):
    model = ProductoCategoria
    form_class = ProductoCategoriaForm
    template_name = "comercio/productocategoria/productocategoria_form.html"
    success_url = reverse_lazy("comercio:productocategoria_list")


class ProductoCategoriaDelete(DeleteView):
    model = ProductoCategoria
    template_name = "comercio/productocategoria/productocategoria_confirm_delete.html"
    success_url = reverse_lazy("comercio:productocategoria_list")
