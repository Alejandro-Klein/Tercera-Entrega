from django import forms

class CrearAlumnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=20)
    materia= forms.CharField(max_length=20)

class BuscarAlumnoFormulario(forms.Form):
    nombre= forms.CharField(max_length=20,required=False)
    
