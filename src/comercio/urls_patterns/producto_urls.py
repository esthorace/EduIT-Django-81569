from django.urls import path

from ..views import producto_crud

urlpatterns = [
    path("", producto_crud.Index.as_view(), name="index"),
    path(
        "producto/list",
        producto_crud.ProductoCatergoriaList.as_view(),
        name="producto_list",
    ),
    path(
        "producto/create",
        producto_crud.ProductoCreate.as_view(),
        name="producto_create",
    ),
    path(
        "producto/detail/<int:pk>",
        producto_crud.ProductoDetail.as_view(),
        name="producto_detail",
    ),
    path(
        "producto/update/<int:pk>",
        producto_crud.ProductoUpdate.as_view(),
        name="producto_update",
    ),
    path(
        "producto/delete/<int:pk>",
        producto_crud.ProductoDelete.as_view(),
        name="producto_delete",
    ),
]
