from django.urls import path
from inicio import views # me traigo las views

app_name = "inicio" # Identifico un nombre para que cuando navegue por los pat si tengo muchas app 
                    # con la mismos nombre para navegar se vuelve el error ahora voy al base.html
                    # y corrijo la navegacion para indicar q es para esta app exclusiva.

urlpatterns = [
    path("", views.inicio ,name="inicio"),# al ser una lista debo usar siempre las comas para agregar path.
    path("prueba/", views.prueba,name="prueba"),
    path("usuario/", views.usuario,name="usuario"),
    path("fecha-actual/", views.fecha_actual,name="fecha_actual"),
    path("saludar/", views.saludar,name="saludar" ), # Sin pasar info.
    path("bienvenida/<str:nombre>", views.bienvenida ,name="bienvenida"), # Pasando info.
    #v1 crear alumno
    #path("crear-alumno/<str:nombre>/<str:curso>", views.crear_alumno,name="crear_alumno" )
    #v2 crear alumno
    path("alumnos/", views.lista_alumnos,name="lista_alumnos"),
    path("alumno/crear/", views.crear_alumno,name="crear_alumno"),
]

# el name identifica al path y nos permite acceder por ese nombre.