from importlib import import_module
from django.shortcuts import render
#from config.web.formularios.formularioempleados import FormularioEmpleados

from web.formularios.formularioplatos import FormularioPlatos
from web.formularios.formularioempleados import FormularioEmpleados

from web.models import Platos
from web.models import Empleados

# Create your views here.
#TODAS LAS VISTAS SON FUNCIONES DE PYTHON

def Home(request):
    return render(request,'home.html')

def PlatosVista(request):

    #rutina para consulta de platos
    platosConsultados=Platos.objects.all()
    print(platosConsultados)


    #Esta vista utilizara un formulario django
    #Debor crear un objeto de la clase FormularioPlatos()
    formulario=FormularioPlatos()

    #Creamos un diccionario para enviar el formulario al HTML(template)
    data={
        'formulario': formulario,
        'bandera': False,
        'platos': platosConsultados
    }
    
    #RECIBIMOS LOS DATOS DEL FORMULARIO
    if request.method=="POST":
        datosFormulario=FormularioPlatos(request.POST)
        if datosFormulario.is_valid():
            datosLimpios=datosFormulario.cleaned_data
            print(datosLimpios)
            
            #Contruir un diccionario de envio de datos hacia la BD
            platoNuevo=Platos(
                nombre=datosLimpios["nombre"],
                descripcion=datosLimpios["descripcion"],
                fotografia=datosLimpios["fotografia"],
                precio=datosLimpios["precio"],
                tipo=datosLimpios["tipo"]
            )
            #Intentare llevar mis datos a BD
            try: 
                platoNuevo.save()
                data["bandera"]=True
                print("Exito guardando...")
            except Exception as error:
                print("Upss", error)
                
    
    return render(request, 'menuplatos.html', data)

def EmpleadoVista(request):

    empleadosConsultados=Empleados.objects.all()
    print(empleadosConsultados)

    formularioe=FormularioEmpleados()
    data={
        'formularioe': formularioe,
        'bandera': False,
        'empleados': empleadosConsultados
    }
    
    if request.method=="POST":
        datosFormulario=FormularioEmpleados(request.POST)
        if datosFormulario.is_valid():
            datosLimpiose=datosFormulario.cleaned_data
            print(datosLimpiose)
            
            #CONSTRUIR UN DICCIONARIO DE ENVIO DE DATOS HACIA LA DB
            empleadoNuevo=Empleados(
                nombre=datosLimpiose["nombre"],
                apellidos=datosLimpiose["apellidos"],
                fotografia=datosLimpiose["fotografia"],
                cargo=datosLimpiose["cargo"],
                salario=datosLimpiose["salario"],
                contacto=datosLimpiose["contacto"]
            )
            try: 
                empleadoNuevo.save()
                data["bandera"]=True
                print("Exito guardando...")
            except Exception as error:
                print("Upss", error)
            
    return render(request, 'empleados.html', data)
