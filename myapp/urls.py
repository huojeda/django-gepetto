from django.urls import path
from . import views

urlpatterns = [
    # Rutas para vistas de paginas principales
    path('', views.index, name='index'),  # Página principal (index.html)
    path('quienesSomos/', views.quienesSomos, name='quienesSomos'),
    path('carro/', views.carro, name='carro'),
    path('contacto/', views.contacto, name='contacto'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),

    # Rutas para vistas de paginas categorias
    path('categorias/', views.categorias, name='categorias'),
    path('mesas/', views.mesas, name='mesas'),
    path('rack/', views.rack, name='rack'),
    path('repisas/', views.repisas, name='repisas'),
    path('tablas/', views.tablas, name='tablas'),

    # Rutas para vistas de paginas productos
    path('bar/', views.bar, name='bar'),
    path('black/', views.black, name='black'),
    path('clasica/', views.clasica, name='clasica'),
    path('comoda/', views.comoda, name='comoda'),
    path('estante/', views.estante, name='estante'),
    path('franjas/', views.franjas, name='franjas'),
    path('fullmadera/', views.fullmadera, name='fullmadera'),
    path('metal/', views.metal, name='metal'),
    path('oriental/', views.oriental, name='oriental'),
    path('roble/', views.roble, name='roble'),
    path('rustico/', views.rustico, name='rustico'),
    path('simple/', views.simple, name='simple'),



]