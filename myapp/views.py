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
from django.shortcuts import render, redirect
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

#LOGOUT
# views.py
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

def carro(request):
    return render(request, 'myapp/carro.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')



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






