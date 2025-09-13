from django import forms

from .models import Producto, ProductoCategoria


class ProductoCategoriaForm(forms.ModelForm):
    class Meta:
        model = ProductoCategoria
        # fields = ["nombre"]
        fields = "__all__"

    def clean(self):
        import re

        clean_data = super().clean()
        nombre = clean_data.get("nombre")
        if nombre:
            if len(nombre) < 3:
                raise forms.ValidationError(
                    "El nombre debe contener al menos 3 caracteres"
                )
            if not re.fullmatch(r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü ]+$", nombre):
                raise forms.ValidationError(
                    "El nombre solo debe contener letras, sin números ni espacios"
                )
        return clean_data


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"
