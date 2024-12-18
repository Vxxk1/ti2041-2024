from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect
from productos.views import login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include('productos.urls')),
    path('login/', login_view, name='login'),  
    path('logout/', logout_view, name='logout'),
    path('', lambda request: HttpResponseRedirect('login/')),
]
