from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Lista de productos
    path('registrar/', views.register_product, name='register_product'),  # Registrar producto
    path('resultado/<int:producto_id>/', views.result, name='result'),  # Resultado del registro
]
