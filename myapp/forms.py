# myapp/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

#REGISTRO
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # Validación personalizada de contraseñas
    def clean(self):
        cleaned_data = super().clean()  # Llama al método `clean` de la clase base
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            raise forms.ValidationError("Las contraseñas no coinciden.")

        return cleaned_data


#INFORMACION DE CLIENTES
#cliente
from .models import (Cliente,
                    Medio_de_Pago,
                     Comuna,
                     Region)

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'rut_cliente', 'telefono', 'fecha_nacimiento', 'genero', 'edad']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Si estamos editando una instancia existente
            self.fields['rut_cliente'].widget.attrs['readonly'] = True  # Hacer el campo 'rut_cliente' solo lectura

    # Opcional: puedes agregar validaciones personalizadas si es necesario

#direccion
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['direccion', 'comuna', 'region']

    # Aquí también se pueden agregar validaciones si es necesario

#from .models import Medio_de_Pago

class MedioDePagoForm(forms.ModelForm):
    class Meta:
        model = Medio_de_Pago
        fields = ['banco', 'tipo_de_cuenta', 'numero']

