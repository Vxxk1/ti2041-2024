from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm

# Vista para listar productos con filtro por nombre
def index(request):
    # Obtener todos los productos
    productos = Producto.objects.all()

    # Obtener el parámetro de filtrado por nombre
    nombre = request.GET.get('nombre')

    # Aplicar el filtro si existe
    if nombre:
        productos = productos.filter(nombre__icontains=nombre)  # Filtrar por nombre

    # Renderizar la página con los productos filtrados
    return render(request, 'productos/index.html', {'productos': productos})

# Vista para registrar un producto
def register_product(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()  # Guardar el producto en la base de datos
            return redirect('result', producto_id=producto.id)  # Redirigir a la pantalla de resultado
    else:
        form = ProductoForm()
    return render(request, 'productos/registro.html', {'form': form})

# Vista para mostrar el resultado de la creación de un producto
def result(request, producto_id):
    producto = Producto.objects.get(id=producto_id)  # Obtener el producto por su ID
    return render(request, 'productos/resultado.html', {'producto': producto})
