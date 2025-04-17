

# Create your views here.
from django.shortcuts import render

#paginas principales
def index(request):
    return render(request, 'myapp/index.html')

def carro(request):
    return render(request, 'myapp/carro.html')

def contacto(request):
    return render(request, 'myapp/contacto.html')

def login(request):
    return render(request, 'myapp/login.html')

def quienesSomos(request):
    return render(request, 'myapp/quienesSomos.html')

def registro(request):
    return render(request, 'myapp/registro.html')

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






