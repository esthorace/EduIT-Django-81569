from django.db import models


class ProductoCategoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(verbose_name="descripción", blank=True, null=True)

    def __str__(self) -> str:
        return self.nombre

    class Meta:
        verbose_name = "Categoría de Producto"
        verbose_name_plural = "Categorías de Productos"


class Producto(models.Model):
    producto_categoria = models.ForeignKey(
        ProductoCategoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="categoría",
    )
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(verbose_name="descripción", blank=True, null=True)
    unidad_medida = models.CharField(max_length=50)
    stock = models.FloatField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(editable=False, auto_now=True)

    def __str__(self) -> str:
        return f"{self.nombre} ({self.unidad_medida}) ${self.precio:.2f}"

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        unique_together = ("producto_categoria", "nombre")


# bebidas, agua
# bebidas, agua -> error

# bebidas, agua
# null ,   agua  -> ok
