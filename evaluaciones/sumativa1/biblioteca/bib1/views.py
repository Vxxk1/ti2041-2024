from django.shortcuts import render

def productos_view(request):
    return render(request, 'productos.html')
