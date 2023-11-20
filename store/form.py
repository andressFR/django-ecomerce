from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

"""archivo qque nos servira para la creacion del formulario de 
registro pra los usuarios"""

class CustomUserForm(UserCreationForm):
    #Campos del formulario
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Ingresa un usuario'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Ingresa un correo'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Ingresa una contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirmar contraseña'}))

    class Meta:
        model = User
        #campos del formulario
        fields = ['username','email','password1','password2']
