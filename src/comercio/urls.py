from .urls_patterns import producto_urls, productocategoria_urls

app_name = "comercio"

urlpatterns = [
    *productocategoria_urls.urlpatterns,
    *producto_urls.urlpatterns,
]
