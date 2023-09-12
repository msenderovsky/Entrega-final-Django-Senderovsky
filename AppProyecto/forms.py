from django import forms

class ActorFormulario(forms.Form):
    nombre= forms.CharField(max_length=10)
    apellido= forms.CharField(max_length=10)

class DirectorFormulario(forms.Form):
    nombre= forms.CharField(max_length=10)
    apellido= forms.CharField(max_length=10)

class PeliFormulario(forms.Form):
    nombre= forms.CharField(max_length=10)
    año= forms.IntegerField()
    director= forms.CharField(max_length=10)
    productora= forms.CharField(max_length=10)
