from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context

# V1
# def inicio(request):
#    return HttpResponse("Hola soy INICIO") # pongo lo que quiero que muestre la view

def inicio(request):
    
   archivo = open(r"C:\Users\Ale\Desktop\CODERHOUSE\mi-django\templates\inicio.html", "r")
  
   template = Template(archivo.read())
   
   archivo.close()
   
   contexto = Context()
   
   renderizar_template = template.render(contexto)
    
   return HttpResponse(renderizar_template)

def usuario(request):
    return HttpResponse("<h1>Hola soy USUARIO</h1>")

def fecha_actual(request):
    
    fecha = datetime.now()
    
    return HttpResponse(f"FECHA ACTUAL: {fecha}")

def saludar(request):
    return HttpResponse("BIENVENIDO/A!!!")

def bienvenida(request,nombre):
    return HttpResponse(f"BIENVENIDO/A  {nombre.title()}!!!") # con esto le paso lo que escriba en la url como nombre.Pueden ser mas.

# Las vistas deben tener siempre nombres diferentes.