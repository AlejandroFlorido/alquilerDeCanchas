from django.shortcuts import render, redirect
from .models import Cancha
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required

def homepage(request):
    
    return render(request, 'Home.html')

def alquiler(request):
    
    return render(request, 'Alquiler.html')

def canchas(request):
    
    canchas = Cancha.objects.all()

    return render(request, 'Canchas.html', {"canchas" : canchas})

def exit(request):
    
    logout(request)

    return redirect('inicio')