Endpoints API Lista de Productos
URL: http://127.0.0.1:8000/api/productos/
Descripcion: Retorna todos los productos y su precio
Respuesta:
HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "nombre_producto": "Clasica",
        "precio": "50000.00"
    },
    {
        "nombre_producto": "Franjas",
        "precio": "60000.00"
    },
    {
        "nombre_producto": "Oriental",
        "precio": "70000.00"
    },
    {
        "nombre_producto": "Estante",
        "precio": "500000.00"
    },
    {
        "nombre_producto": "Comoda",
        "precio": "430000.00"
    },
    {
        "nombre_producto": "Bar",
        "precio": "400000.00"
    },
    {
        "nombre_producto": "Rustico",
        "precio": "380000.00"
    },
    {
        "nombre_producto": "Simple",
        "precio": "300000.00"
    },
    {
        "nombre_producto": "Metal",
        "precio": "400000.00"
    },
    {
        "nombre_producto": "FullMadera",
        "precio": "700000.00"
    },
    {
        "nombre_producto": "Black",
        "precio": "550000.00"
    },
    {
        "nombre_producto": "Roble",
        "precio": "650000.00"
    }
]

Endpoints API Publcidad
URL: http://127.0.0.1:8000/api/publicidad/
Descripcion: Retorna imagenes de los productos para hacer publicidad
Respuesta:

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "titulo": "Repisa Comoda",
        "imagen_url": "/static/img/comoda1.jpg"
    },
    {
        "titulo": "Repisa Bar",
        "imagen_url": "/static/img/bar1.jpg"
    },
    {
        "titulo": "Repisa Estante",
        "imagen_url": "/static/img/estante1.jpg"
    },
    {
        "titulo": "Rack Rustico",
        "imagen_url": "/static/img/rustico1.jpg"
    },
    {
        "titulo": "Rack Simple",
        "imagen_url": "/static/img/simple1.jpg"
    },
    {
        "titulo": "Mesa Full Madera",
        "imagen_url": "/static/img/fullmadera1.jpg"
    },
    {
        "titulo": "Mesa Black",
        "imagen_url": "/static/img/black1.jpg"
    },
    {
        "titulo": "Mesa Roble",
        "imagen_url": "/static/img/roble1.jpg"
    },
    {
        "titulo": "Tabla Clasica",
        "imagen_url": "/static/img/clasica1.jpg"
    },
    {
        "titulo": "Tabla franjas",
        "imagen_url": "/static/img/franjas1.jpg"
    },
    {
        "titulo": "Tabla Oriental",
        "imagen_url": "/static/img/oriental1.jpg"
    },
    {
        "titulo": "Rack Metal",
        "imagen_url": "/static/img/metal1.jpg"
    }
]
