from django.shortcuts import render, redirect
from .models import Cancha
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def homepage(request):
    
    return render(request, 'Home.html')

@login_required

def alquiler(request):
    
    return render(request, 'Alquiler.html')

@login_required

def canchas(request):
    
    canchaslistadas = Cancha.objects.all()

    return render(request, 'Canchas.html', {"canchaslistadas" : canchaslistadas})

def exit(request):
    
    logout(request)

    return redirect('inicio')

def registrarcancha(request):

    Nombre_cancha=request.POST['txtNombre']
    id_cancha=request.POST['numberID']
    tipo=request.POST['txtTipo']
    disponible=True
    con_luz=False
    horario_reservado=False
    duracion_reserva=request.POST['numberdu']

    cancha= Cancha.objects.create(Nombre_cancha=Nombre_cancha, id_cancha=id_cancha, tipo=tipo, disponible=disponible, con_luz=con_luz, horario_reservado=horario_reservado, duracion_reserva=duracion_reserva)

    return redirect('canchas')