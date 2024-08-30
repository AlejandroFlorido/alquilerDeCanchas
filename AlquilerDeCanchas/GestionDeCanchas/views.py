from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def homepage(request):
    
    return render(request, 'Home.html')

@login_required

def alquiler(request):
    
    return render(request, 'Alquiler.html')

def canchas(request):
    
    return render(request, 'Canchas.html')

def exit(request):
    
    logout(request)

    return redirect('inicio')