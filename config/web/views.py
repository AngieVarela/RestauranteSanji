from importlib import import_module
from django.shortcuts import render
#from config.web.formularios.formularioempleados import FormularioEmpleados

from web.formularios.formularioplatos import FormularioPlatos
from web.formularios.formularioempleados import FormularioEmpleados

# Create your views here.
#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def Platos(request):
    #Esta vista utilizara un formulario django
    #Debor crear un objeto de la clase FormularioPlatos()
    formulario=FormularioPlatos()

    #Creamos un diccionario para enviar el formulario al HTML(template)
    data={
        'formulario': formulario
    }
    return render(request, 'menuplatos.html', data)

def Empleados(request):
    formularioe=FormularioEmpleados()
    data={
        'formularioe': formularioe
    }
    return render(request, 'empleados.html', data)
