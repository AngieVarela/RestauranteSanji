from django.shortcuts import render

# Create your views here.
#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')
