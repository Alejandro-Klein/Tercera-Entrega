from django.urls import path
from inicio import views # me traigo las views

urlpatterns = [
    path("", views.inicio),# al ser una lista debo usar siempre las comas para agregar path.
    path("prueba/", views.prueba),
    path("usuario/", views.usuario),
    path("fecha-actual/", views.fecha_actual),
    path("saludar/", views.saludar ), # Sin pasar info.
    path("bienvenida/<str:nombre>", views.bienvenida ), # Pasando info.
    path("crear-alumno/<str:nombre>/<str:curso>", views.crear_alumno )
]
