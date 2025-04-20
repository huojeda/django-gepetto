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

from django import forms
from .models import Cliente
import re
from datetime import date


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'rut_cliente', 'telefono', 'fecha_nacimiento', 'genero', 'edad']

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:  # Si estamos editando una instancia existente
            self.fields['rut_cliente'].widget.attrs['readonly'] = True  # Hacer el campo 'rut_cliente' solo lectura

    def clean_rut_cliente(self):
        rut = self.cleaned_data.get('rut_cliente')
        # Validar el formato de RUT (ejemplo de validación básica)
        if not re.match(r'^\d{1,2}\.\d{3}\.\d{3}-[\dkK]$', rut):
            raise forms.ValidationError("El RUT no tiene un formato válido. (12.345.678-9).")

        # Validación de unicidad para asegurarse que el RUT no se repita
        if Cliente.objects.filter(rut_cliente=rut).exclude(id=self.instance.id).exists():
            raise forms.ValidationError("Este RUT ya está registrado.")

        return rut

    def clean_edad(self):
        edad = self.cleaned_data.get('edad')
        # Validar que la edad sea un número positivo
        if edad <= 0:
            raise forms.ValidationError("La edad debe ser un número mayor que 0.")
        return edad

    def clean_fecha_nacimiento(self):
        fecha_nacimiento = self.cleaned_data.get('fecha_nacimiento')
        # Validar que la fecha de nacimiento no sea una fecha futura
        if fecha_nacimiento > date.today():
            raise forms.ValidationError("La fecha de nacimiento no puede ser una fecha futura.")
        return fecha_nacimiento



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

