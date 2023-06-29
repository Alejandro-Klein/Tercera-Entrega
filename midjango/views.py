from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader

# V1
# def inicio(request):
#    return HttpResponse("Hola soy INICIO") # pongo lo que quiero que muestre la view

#v2
# def inicio(request):
    
#    archivo = open(r"C:\Users\Ale\Desktop\CODERHOUSE\mi-django\templates\inicio.html", "r") 
  
#    template = Template(archivo.read()) #Template de solo texto.
   
#    archivo.close()
   
#    segundos = datetime.now().second
   
#    diccionario = {
#        "mensaje": "Este es el msj de Inicio...", # Esto se lo debo pasar al inicio.html
#        "segundos": segundos,
#        "segundos_par": segundos%2 ==0,
#        "listado_de_numeros": list(range(25))
#    }
   
#    contexto = Context(diccionario) # es la info que quiero que reciba el template.
#    renderizar_template = template.render(contexto) # esto es para q lo lea el httpresponse
#    return HttpResponse(renderizar_template)

#v1
def inicio(request):
   #no me conviene tener esta direccion por el que se baje el mismo capas no la tenga
   template = loader.get_template("inicio.html") # carga el tamplate
   segundos = datetime.now().second
   diccionario = {
       "mensaje": "Este es el msj de Inicio...", # Esto se lo debo pasar al inicio.html
       "segundos": segundos,
       "segundos_par": segundos%2 ==0,
       "listado_de_numeros": list(range(25))
   }
   
   renderizar_template  = template.render(diccionario)
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