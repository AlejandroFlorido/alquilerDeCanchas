"""
URL configuration for AlquilerDeCanchas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from GestionDeCanchas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name="inicio"),
    path('Alquiler/', views.alquiler, name="alquiler"),
    path('Canchas/', views.canchas, name="canchas"),
    path('accounts/', include('django.contrib.auth.urls'), name="login"),
    path('logout/', views.exit, name="exit"),
    path('registrarcancha/', views.registrarcancha, name="registrarcancha"),
    path('Canchas/eliminarcancha/<id_cancha>', views.eliminarcancha, name="eliminarcancha"),
    path('Canchas/edicioncancha/<id_cancha>', views.edicioncancha, name="edicioncancha"),
    path('editarcancha/', views.editarcancha, name="editarcancha"),
    path('Clientes/', views.clientes, name="clientes"),
    path('registrarcliente/', views.registrarcliente, name="registrarcliente"),
    path('Clientes/eliminarcliente/<dni>', views.eliminarcliente, name="eliminarcliente"),
    path('Clientes/edicioncliente/<dni>', views.edicioncliente, name="edicioncliente"),
    path('editarcliente/', views.editarcliente, name="editarcliente"),
]
