from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Categoria, Producto

# Registrar el modelo Categoria
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id_categoria', 'nombre_categoria')  # Campos a mostrar en la lista
    search_fields = ('nombre_categoria',)  # Campo en el que se puede hacer búsqueda en el admin

# Registrar el modelo Producto
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id_producto', 'nombre_producto', 'precio', 'stock', 'nombre_categoria')  # Campos a mostrar
    search_fields = ('nombre_producto',)  # Campo para búsqueda
    list_filter = ('nombre_categoria',)  # Filtros para categorías
    ordering = ('-precio',)  # Ordenar los productos por precio de mayor a menor
