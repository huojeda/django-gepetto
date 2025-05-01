from rest_framework import serializers
from .models import Producto, Publicidad

#API lista de productos
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre_producto', 'precio']

#API publicidad
class PublicidadSerializer(serializers.ModelSerializer):
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Publicidad
        fields = ['titulo', 'imagen_url']

    def get_imagen_url(self, obj):
        return f'/static/img/{obj.imagen_nombre}' if obj.imagen_nombre else None