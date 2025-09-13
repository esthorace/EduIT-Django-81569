from django.contrib import admin

from .models import Producto, ProductoCategoria

admin.site.register(ProductoCategoria)
admin.site.register(Producto)
