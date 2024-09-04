from django.shortcuts import render, redirect
from .models import Cancha, Cliente
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages

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

@login_required

def clientes(request):
    
    clienteslistados = Cliente.objects.all()

    return render(request, 'Clientes.html', {"clienteslistados" : clienteslistados})

def exit(request):
    
    logout(request)

    return redirect('inicio')

def registrarcancha(request):

    Nombre_cancha=request.POST['txtNombre']
    tipo=request.POST['txtTipo']
    disponible=True
    con_luz=False
    horario_reservado=False
    duracion_reserva=request.POST['numberdu']

    cancha= Cancha.objects.create(Nombre_cancha=Nombre_cancha, tipo=tipo, disponible=disponible, con_luz=con_luz, horario_reservado=horario_reservado, duracion_reserva=duracion_reserva)

    messages.success(request, 'Se ha registrado una cancha')

    return redirect('canchas')

def edicioncancha(request, id_cancha):

    cancha = Cancha.objects.get(id_cancha=id_cancha)

    return render(request, 'Edicioncancha.html', {"cancha":cancha})

def editarcancha(request):

    Nombre_cancha=request.POST['txtNombre']
    id_cancha=request.POST['numberID']
    tipo=request.POST['txtTipo']
    duracion_reserva=request.POST['numberdu']

    cancha = Cancha.objects.get(id_cancha=id_cancha)
    cancha.Nombre_cancha = Nombre_cancha
    cancha.tipo = tipo
    cancha.duracion_reserva = duracion_reserva

    cancha.save()

    messages.success(request, 'Se ha editado con exito la cancha seleccionada')

    return redirect('canchas')    

def eliminarcancha(request, id_cancha):
    
    cancha = Cancha.objects.get(id_cancha=id_cancha)

    cancha.delete()

    messages.success(request, 'Se ha eliminado la cancha seleccionada')

    return redirect('canchas')

def registrarcliente(request):

    Nombre_completo=request.POST['txtNombre']
    dni=request.POST['numberdni']
    telefono=request.POST['numbertel']
    email=request.POST['email']

    cliente= Cliente.objects.create(Nombre_completo=Nombre_completo, dni=dni, telefono=telefono, email=email)

    messages.success(request, 'Se ha registrado un cliente')

    return redirect('clientes')

def edicioncliente(request, dni):

    cliente = Cliente.objects.get(dni=dni)

    return render(request, 'Edicioncliente.html', {"cliente":cliente})

def editarcliente(request):

    Nombre_completo=request.POST['txtNombre']
    dni=request.POST['numberdni']
    telefono=request.POST['numbertel']
    email=request.POST['email']

    cliente = Cliente.objects.get(dni=dni)
    cliente.Nombre_completo = Nombre_completo
    cliente.telefono = telefono
    cliente.email = email

    cliente.save()

    messages.success(request, 'Se ha editado con exito el cliente seleccionado')

    return redirect('clientes')    

def eliminarcliente(request, dni):
    
    cliente = Cliente.objects.get(dni=dni)

    cliente.delete()

    messages.success(request, 'Se ha eliminado el cliente seleccionado')

    return redirect('clientes')
    