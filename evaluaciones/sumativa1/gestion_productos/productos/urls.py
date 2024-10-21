from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar/', views.register_product, name='register_product'), 
    path('resultado/<int:producto_id>/', views.result, name='result'), 
]
