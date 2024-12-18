from ninja import NinjaAPI, Schema
from django.contrib.auth import authenticate
from django.http import HttpRequest, Http404
from django.shortcuts import get_object_or_404
from pydantic import ValidationError
from .models import Producto, Marca, Categoria, Caracteristica
from .utils import generar_token, JWTAuth
from typing import List

api = NinjaAPI(
    title="API productos",
    description="Servicios para productos",
    version="1.0.0"
)

auth = JWTAuth()

# Manejadores de Errores
@api.exception_handler(Http404)
def error_404(request, ex):
    return api.create_response(request, 
                            {'response': 'Recurso no encontrado'},
                            status=404)
    
@api.exception_handler(ValidationError)
def error_validacion(request, ex):
    return api.create_response(request,
                            {
                                'response': 'Error de Formato de Entrada',
                                'errores': ex.errors()
                            },
                            status=422)

class AuthRequest(Schema):
    username: str
    password: str

@api.post(path="/token", tags=["Auth"])
def get_token(request, data: AuthRequest):
    user = authenticate(username=data.username, password=data.password)
    if not user:
        return { "error": "Credenciales inválidas" }
    token = generar_token(user)
    return { "token": token }

@api.get(path="productos/", tags=["Products"])
def obtener_productos(request):
    all_products = Producto.objects.all().values()
    return list(all_products)

@api.get(path="productos/{codigo}", tags=["Products"])
def obtener_producto(request, codigo: str):
    all_products = Producto.objects.filter(codigo=codigo).values()
    return list(all_products)

class ProductSchema(Schema):
    nombre: str
    precio: float
    marca: int
    categoria: int = None
    caracteristicas: List[int] = []

@api.post(path="productos/", auth=auth, tags=["Products"])
def agregar_producto(request, data: ProductSchema):
    marca = Marca.objects.get(pk=data.marca)
    categoria = Categoria.objects.get(pk=data.categoria) if data.categoria else None
    producto = Producto(
        nombre=data.nombre,
        precio=data.precio,
        marca=marca,
        categoria=categoria
    )
    producto.save()
    
    # Asociar las características si existen
    for caracteristica_id in data.caracteristicas:
        caracteristica = Caracteristica.objects.get(pk=caracteristica_id)
        producto.caracteristicas.add(caracteristica)

    return {"message": f"{producto.nombre} agregado correctamente"}

@api.put(path="productos/{codigo}", auth=auth, tags=["Products"])
def actualizar_producto(request, codigo: str, data: ProductSchema):
    producto = get_object_or_404(Producto, codigo=codigo)

    # Actualizar los atributos del producto
    for attr, value in data.dict().items():
        if attr == "marca":
            value = get_object_or_404(Marca, id=value)
        elif attr == "categoria" and value:
            value = get_object_or_404(Categoria, id=value)
        setattr(producto, attr, value)
    
    producto.save()

    # Actualizar características
    if data.caracteristicas:
        producto.caracteristicas.clear()
        for caracteristica_id in data.caracteristicas:
            caracteristica = get_object_or_404(Caracteristica, id=caracteristica_id)
            producto.caracteristicas.add(caracteristica)
    
    return {"message": f"{producto.nombre} editado correctamente"}

@api.delete(path="productos/{codigo}", auth=auth, tags=["Products"])
def eliminar_producto(request, codigo: str):
    producto = Producto.objects.filter(codigo=codigo).first()
    if not producto:
        raise Http404("Producto no encontrado")

    producto.delete()
    return {"message": "Producto eliminado exitosamente"}
