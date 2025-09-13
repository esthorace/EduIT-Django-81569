from django.urls import path

from ..views import productocategoria_crud, productocategoria_crud_fbv

urlpatterns = [
    path("", productocategoria_crud_fbv.index, name="index"),
    path(
        "productocategoria/list",
        productocategoria_crud.ProductoCatergoriaList.as_view(),
        name="productocategoria_list",
    ),
    path(
        "productocategoria/create",
        productocategoria_crud.ProductoCategoriaCreate.as_view(),
        name="productocategoria_create",
    ),
    path(
        "productocategoria/detail/<int:pk>",
        productocategoria_crud.ProductoCategoriaDetail.as_view(),
        name="productocategoria_detail",
    ),
    path(
        "productocategoria/update/<int:pk>",
        productocategoria_crud.ProductoCategoriaUpdate.as_view(),
        name="productocategoria_update",
    ),
    path(
        "productocategoria/delete/<int:pk>",
        productocategoria_crud.ProductoCategoriaDelete.as_view(),
        name="productocategoria_delete",
    ),
]
