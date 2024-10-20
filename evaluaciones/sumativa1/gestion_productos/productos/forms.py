from django import forms
from .models import Producto, Caracteristica

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['codigo', 'nombre', 'precio', 'marca', 'categoria', 'caracteristicas']

class CaracteristicaForm(forms.ModelForm):
    class Meta:
        model = Caracteristica
        fields = ['nombre']
