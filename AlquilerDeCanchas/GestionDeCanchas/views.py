from django.shortcuts import render

# Create your views here.

def homepage(request):
    
    return render(request, 'Home.html')

def alquiler(request):
    
    return render(request, 'Alquiler.html')

def canchas(request):
    
    return render(request, 'Canchas.html')