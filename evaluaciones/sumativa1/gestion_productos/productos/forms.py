from django import forms

class ProductoForm(forms.Form):
    codigo = forms.CharField(label='Código', max_length=100)
    nombre = forms.CharField(label='Nombre', max_length=100)
    marca = forms.CharField(label='Marca', max_length=100)
    fecha_vencimiento = forms.DateField(label='Fecha de Vencimiento', widget=forms.SelectDateWidget)
