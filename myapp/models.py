from django.db import models
from django.contrib.auth.models import User

#TABLA COMUNA
class Comuna(models.Model):
    id_comuna = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

#TABLA RGION
class Region(models.Model):
    id_region = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


#TABLA MEDIO DE PAGOS
class Medio_de_Pago(models.Model):
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE,
                                related_name='medios_de_pago')  # Relación con Cliente
    banco = models.CharField(max_length=255)
    tipo_de_cuenta = models.CharField(max_length=255)
    numero = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.banco} - {self.tipo_de_cuenta} - {self.numero}"


#TABLA CLIENTE
class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre_cliente = models.CharField(max_length=255)
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


#TABLA CATEGORIA DE PRODUCTOS
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre_categoria

#TABLA PRODUCTO
class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    nombre_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_producto

#TABLA PARA API PUBLICIDAD
class Publicidad(models.Model):
    titulo = models.CharField(max_length=100)
    imagen_nombre = models.CharField(max_length=100)  # Solo el nombre del archivo, como "promo1.jpg"

    def __str__(self):
        return self.titulo




