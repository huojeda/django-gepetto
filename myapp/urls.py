from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import ProductoListAPIView, PublicidadListAPIView

from . import views

urlpatterns = [
    # Rutas para vistas de paginas principales
    path('', views.index, name='index'),
    path('quienesSomos/', views.quienesSomos, name='quienesSomos'),
    path('contacto/', views.contacto_view, name='contacto'),


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

    # USUARIOS
    path('profile/', views.profile_view, name='profile'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Rutas predeterminadas de autenticación
    path('register/', views.register, name='register'),  # Ruta para el registro
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('cliente/', views.cliente_form, name='cliente_form'),
    path('direccion/', views.direccion_form, name='direccion_form'),
    path('medio_de_pago/', views.medio_de_pago_form, name='medio_de_pago_form'),
    path('mis-datos/', views.mis_datos, name='mis_datos'),

    #CARRO DE COMPRA
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('agregar/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('eliminar/<int:producto_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),

    #API Propia
    path('api/productos/', ProductoListAPIView.as_view(), name='producto-list'),
    path('api/publicidad/', PublicidadListAPIView.as_view(), name='publicidad-list'),

    #API Externa
    path('apiexterna/', views.productos_view, name='apiexterna'),
    path('apiexterna2/', views.conversion_monedas_view, name='conversion_monedas'),



]