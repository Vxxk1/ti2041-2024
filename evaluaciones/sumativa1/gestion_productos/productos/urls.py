from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos_home, name='productos_home'),
    path('registrar/', views.registrar_producto, name='registrar_producto'),
    path('consulta/', views.consulta_productos, name='consulta_productos'),  
]
