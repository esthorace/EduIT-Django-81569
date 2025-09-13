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

from ..forms import ProductoForm
from ..models import Producto


class Index(TemplateView):
    template_name = "comercio/index.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["titulo"] = "Mi Negocio"
        return context


class ProductoCatergoriaList(ListView):
    model = Producto
    template_name = "comercio/producto/producto_list.html"
    # queryset = Producto.objects.all()
    # context_object_name = "object_list"

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        buscar = self.request.GET.get("consulta")
        if buscar:
            queryset = Producto.objects.filter(nombre__icontains=buscar)
        else:
            queryset = Producto.objects.all()
        return queryset


class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = "comercio/producto/producto_form.html"
    success_url = reverse_lazy("comercio:producto_list")


class ProductoDetail(DetailView):
    model = Producto
    template_name = "comercio/producto/producto_detail.html"


class ProductoUpdate(UpdateView):
    model = Producto
    form_class = ProductoForm
    template_name = "comercio/producto/producto_form.html"
    success_url = reverse_lazy("comercio:producto_list")


class ProductoDelete(DeleteView):
    model = Producto
    template_name = "comercio/producto/producto_confirm_delete.html"
    success_url = reverse_lazy("comercio:producto_list")
