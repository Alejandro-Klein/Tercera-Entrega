from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from inicio.models import Alumno
from django.shortcuts import render

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
def prueba(request):
   #no me conviene tener esta direccion larga por el que se baje el mismo capas no la tenga
   segundos = datetime.now().second
   diccionario = {
       "mensaje": "Este es el msj de Inicio...", # Esto se lo debo pasar al inicio.html
       "segundos": segundos,
       "segundos_par": segundos%2 ==0,
       "listado_de_numeros": list(range(25))
   }
   return render(request, "inicio/prueba.html",diccionario)
#    renderizar_template  = template.render(diccionario)
#    return HttpResponse(renderizar_template)
  

def usuario(request):
    return HttpResponse("<h1>Hola soy USUARIO</h1>")

def fecha_actual(request):
    
    fecha = datetime.now()
    
    return HttpResponse(f"FECHA ACTUAL: {fecha}")

def saludar(request):
    return HttpResponse("BIENVENIDO/A!!!")

def bienvenida(request,nombre):
    return HttpResponse(f"BIENVENIDO/A  {nombre.title()}!!!") # con esto le paso lo que escriba en la url como nombre.Pueden ser mas.

#v1
# #def crear_alumno(request,nombre,curso):
#    template = loader.get_template("crear_alumno.html") # carga el tamplate
#    alumno = Alumno(nombre=nombre,curso=curso)
#    alumno.save() # para guardar en BD.
#    diccionario = {
#       "alumno": alumno,
#    }
#    return render(request, "inicio.html" , diccionario) # con esto tengo el inicio cargado
#    renderizar_template  = template.render(diccionario)
#    return HttpResponse(renderizar_template)
    
# Las vistas deben tener siempre nombres diferentes.

#v2
def crear_alumno(request,nombre,curso):
   alumno = Alumno(nombre=nombre,curso=curso)
   alumno.save() # para guardar en BD.
   diccionario = {
      "alumno": alumno,
   }
   return render(request, "inicio/crear_alumno.html" , diccionario) # con esto tengo el inicio cargado

def inicio(request):
 return render(request,"inicio/inicio.html")