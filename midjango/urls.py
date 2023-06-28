"""
URL configuration for midjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from midjango import views # v1 me traigo todo de views
#v2 from midjango.views import inicio,usuario,fecha_actual # traigo lo que necesito de la view, esto es un paquete q tiene l oque quiero.
#v3 from midjango.views import usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.inicio), # al ser una lista debo usar siempre las comas para agregar path.
    path("usuario/", views.usuario),
    path("fecha-actual/", views.fecha_actual),
    path("saludar/", views.saludar ), # Sin pasar info.
    path("bienvenida/<str:nombre>", views.bienvenida ) # Pasando info.
]