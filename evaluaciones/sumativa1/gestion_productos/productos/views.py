from django.shortcuts import render
from .forms import ProductoForm
from django.http import HttpResponse

productos_registrados = [] 

def productos_home(request):
    return render(request, 'productos/index.html') 

def registrar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            
            productos_registrados.append(form.cleaned_data)
            return render(request, 'productos/resultado.html', {'producto': form.cleaned_data})
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form})

def consulta_productos(request):

    return render(request, 'productos/consulta.html', {'productos': productos_registrados})
