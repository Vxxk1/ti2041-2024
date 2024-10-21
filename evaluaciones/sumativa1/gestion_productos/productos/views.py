from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

def index(request):
    productos = Producto.objects.all()

    nombre = request.GET.get('nombre')

    if nombre:
        productos = productos.filter(nombre__icontains=nombre) 

    return render(request, 'productos/index.html', {'productos': productos})

def register_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save() 
            return redirect('result', producto_id=producto.id)
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form})

def result(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'productos/resultado.html', {'producto': producto})
