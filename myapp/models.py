from django.db import models
from django.contrib.auth.models import User


class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


# Definimos la tabla Medio_de_Pago
class Medio_de_Pago(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,
                                related_name='medios_de_pago')  # Relación con Cliente
    banco = models.CharField(max_length=255)
    tipo_de_cuenta = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.banco} - {self.tipo_de_cuenta} - {self.numero}"


# Modelo Cliente actualizado con relación a Comuna, Region y Medio_de_Pago
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    rut_cliente = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()
    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('H', 'Femenino'),
    ]
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    edad = models.IntegerField()
    direccion = models.TextField()

    comuna = models.ForeignKey(Comuna, on_delete=models.SET_NULL, null=True, blank=True)
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} ({self.user.username})"
