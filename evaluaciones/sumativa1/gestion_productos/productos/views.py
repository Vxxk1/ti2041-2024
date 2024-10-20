from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Vista para listar productos
def index(request):
    productos = Producto.objects.all()  # Obtener todos los productos
    return render(request, 'index.html', {'productos': productos})

# Vista para registrar un producto
def register_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()  # Guardar el producto en la base de datos
            return redirect('result', producto_id=producto.id)  # Redirigir a la pantalla de resultado
    else:
        form = ProductoForm()
    return render(request, 'registro.html', {'form': form})

# Vista para mostrar el resultado de la creación de un producto
def result(request, producto_id):
    producto = Producto.objects.get(id=producto_id)  # Obtener el producto por su ID
    return render(request, 'resultado.html', {'producto': producto})
