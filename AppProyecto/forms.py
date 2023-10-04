from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class ActorFormulario(forms.Form):
    nombre= forms.CharField(max_length=10)
    apellido= forms.CharField(max_length=10)

class DirectorFormulario(forms.Form):
    nombre= forms.CharField(max_length=10)
    apellido= forms.CharField(max_length=10)

class PeliFormulario(forms.Form):
    título= forms.CharField(max_length=10)
    año= forms.IntegerField()
    directorNombre= forms.CharField(max_length=10)
    directorApellido= forms.CharField(max_length=10)
    productora= forms.CharField(max_length=10)

class CriticoFormulario(forms.Form):
    nombre= forms.CharField(max_length=10)
    apellido= forms.CharField(max_length=10)
    email= forms.EmailField()

class CriticaFormulario(forms.Form):
    titulo= forms.CharField(max_length=10)
    texto= forms.Textarea()
    critico= forms.EmailField()

class UserEditForm(UserChangeForm):
    password= forms.CharField(
        help_text='',
        widget=forms.HiddenInput(), required=False
    )
    password1= forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    class Meta:
        model= User
        fields=["username", "email"]
    
    def clean_password2(self):
        password1= self.cleaned_data["password1"]
        password2= self.cleaned_data["password2"]
        if password1 != password2:
            raise forms.ValidationError('Las contraseñas no coinciden')
        return password2
