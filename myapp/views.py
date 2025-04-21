from django.shortcuts import render, redirect
from django.contrib.auth import login


from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate


#REGISTRO
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Esto guarda el usuario
            return redirect('login')  # Redirige al login
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

#LOGIN
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Aquí autenticamos al usuario
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)  # Iniciar sesión al usuario
                return redirect('index')  # Redirigir al índice o página principal
            else:
                form.add_error(None, "Nombre de usuario o contraseña incorrectos.")
        # Si el formulario no es válido o hay un error
        return render(request, "myapp/login.html", {"form": form})
    else:
        form = AuthenticationForm()
    return render(request, "myapp/login.html", {"form": form})

#PROFILE
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

@login_required
def profile_view(request):
    if request.method == 'POST':
        # Si se envía el formulario de cambio de contraseña
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            # Actualizamos la sesión para evitar que el usuario se desconecte al cambiar la contraseña
            update_session_auth_hash(request, form.user)
            return redirect('profile')  # Redirigimos al perfil después del cambio de contraseña
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'myapp/profile.html', {'form': form})

#INFO CLIENTE
from .forms import ClienteForm, DireccionForm, MedioDePagoForm
from .models import Region
from .models import Comuna
from .models import Medio_de_Pago
from .models import Cliente
from django.contrib.auth.decorators import login_required

@login_required
def cliente_form(request):
    try:
        cliente = Cliente.objects.get(user=request.user)  # Obtener el cliente logueado
    except Cliente.DoesNotExist:
        cliente = None  # Si no existe, establecemos cliente a None

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            cliente = form.save(commit=False)
            cliente.user = request.user  # Asociamos el cliente al usuario logeado
            cliente.save()
            return redirect('mis_datos')  # Redirigimos a mis datos
    else:
        form = ClienteForm(instance=cliente)

    return render(request, 'myapp/cliente_form.html', {'form': form})


#INFO DIRECCION
@login_required
def direccion_form(request):
    cliente = Cliente.objects.get(user=request.user)  # Obtenemos el cliente logeado

    if request.method == 'POST':
        form = DireccionForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('mis_datos')  # Redirigimos a mis datos
    else:
        form = DireccionForm(instance=cliente)

    return render(request, 'myapp/direccion_form.html', {'form': form})

#INFO MEDIO DE PAGO
@login_required
def medio_de_pago_form(request):
    if request.method == 'POST':
        form = MedioDePagoForm(request.POST)
        if form.is_valid():
            medio_de_pago = form.save(commit=False)
            medio_de_pago.cliente = Cliente.objects.get(user=request.user)  # Asociamos el medio de pago al cliente
            medio_de_pago.save()
            return redirect('mis_datos')  # Redirigimos a mis datos
    else:
        form = MedioDePagoForm()

    return render(request, 'myapp/medio_de_pago_form.html', {'form': form})

#MIS DATOS
# myapp/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import (Cliente,
                     Medio_de_Pago)
from .forms import ClienteForm, DireccionForm, MedioDePagoForm

@login_required
def mis_datos(request):
    try:
        cliente = Cliente.objects.get(user=request.user)  # Obtener el cliente asociado al usuario logueado
    except Cliente.DoesNotExist:
        return redirect('cliente_form')  # Si no existe, redirige al formulario de cliente

    # Obtener el medio de pago
    medio_de_pago = Medio_de_Pago.objects.filter(cliente=cliente).first()

    return render(request, 'myapp/misdatos.html', {
        'cliente': cliente,
        'medio_de_pago': medio_de_pago,
    })

#CONTACTO
from django.shortcuts import render
from .forms import ContactoForm

def contacto_view(request):
    form = ContactoForm()
    return render(request, 'myapp/contacto.html', {'form': form})


#LOGOUT
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    # Cierra la sesión del usuario
    logout(request)
    # Redirige
    return render(request, 'registration/logout.html')


#paginas principales
def index(request):
    return render(request, 'myapp/index.html')







def quienesSomos(request):
    return render(request, 'myapp/quienesSomos.html')



#paginas categorias
def categorias(request):
    return render(request, 'myapp/categorias/categorias.html')

def mesas(request):
    return render(request, 'myapp/categorias/mesas.html')

def rack(request):
    return render(request, 'myapp/categorias/rack.html')

def repisas(request):
    return render(request, 'myapp/categorias/repisas.html')

def tablas(request):
    return render(request, 'myapp/categorias/tablas.html')

#paginas productos
def bar(request):
    return render(request, 'myapp/productos/bar.html')

def black(request):
    return render(request, 'myapp/productos/black.html')

def clasica(request):
    return render(request, 'myapp/productos/clasica.html')

def comoda(request):
    return render(request, 'myapp/productos/comoda.html')

def estante(request):
    return render(request, 'myapp/productos/estante.html')

def franjas(request):
    return render(request, 'myapp/productos/franjas.html')

def fullmadera(request):
    return render(request, 'myapp/productos/fullmadera.html')

def metal(request):
    return render(request, 'myapp/productos/metal.html')

def oriental(request):
    return render(request, 'myapp/productos/oriental.html')

def roble(request):
    return render(request, 'myapp/productos/roble.html')

def rustico(request):
    return render(request, 'myapp/productos/rustico.html')

def simple(request):
    return render(request, 'myapp/productos/simple.html')

#CARRO DE COMPRA
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto

# Inicializa el carrito si no existe
def _init_carrito(request):
    if 'carrito' not in request.session:
        request.session['carrito'] = {}

from django.contrib import messages
# Agrega producto al carrito
def agregar_al_carrito(request, producto_id):
    _init_carrito(request)
    carrito = request.session['carrito']
    producto_id = str(producto_id)

    if producto_id in carrito:
        carrito[producto_id] += 1
    else:
        carrito[producto_id] = 1

    request.session.modified = True
    return redirect('ver_carrito')

# Elimina producto del carrito
def eliminar_del_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id = str(producto_id)

    if producto_id in carrito:
        del carrito[producto_id]
        request.session.modified = True

    return redirect('ver_carrito')

# Muestra el carrito
def ver_carrito(request):
    _init_carrito(request)
    carrito = request.session.get('carrito', {})
    productos = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id_producto=int(producto_id))
        subtotal = producto.precio * cantidad
        productos.append({
            'id': producto.id_producto,
            'nombre': producto.nombre_producto,
            'precio': producto.precio,
            'cantidad': cantidad,
            'subtotal': subtotal
        })
        total += subtotal

    return render(request, 'myapp/carro.html', {'items': productos, 'total': total})

#API CLIMA
# views.py
import requests
from django.shortcuts import render

def index(request):
    clima = {}
    ciudad = 'Santiago'
    url = f'https://wttr.in/{ciudad}?format=j1'

    try:
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            data = respuesta.json()
            clima = {
                'ciudad': ciudad,
                'temperatura': data['current_condition'][0]['temp_C'],
                'descripcion': data['current_condition'][0]['weatherDesc'][0]['value']
            }
    except:
        clima = None

    return render(request, 'myapp/index.html', {'clima': clima})
