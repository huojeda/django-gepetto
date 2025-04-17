$(document).ready(function () {
  
    $("form").submit(function (event) {
        event.preventDefault(); 

       
        $(".text-danger").text(""); 
        $("#mensaje-exito").hide(); 

        
        var formulario = $(this).attr("id");

        
        if (formulario === "formulario_contacto") {
            
            var nombre = $("#nombre").val();
            var nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;
            if (nombre === "") {
                $("#nombre-error").text("Por favor, ingrese un nombre válido.");
                return;
            }
            if (!nombreRegex.test(nombre)) {
                $("#nombre-error").text("Por favor, ingrese solo letras en el nombre.");
                return;
            }

            
            if ($("#direccion").val() === "") {
                $("#direccion-error").text("Por favor, ingrese una dirección válida.");
                return;
            }

            
            var telefono = $("#fono").val();
            var telefonoRegex = /^[0-9]+$/;
            if (telefono === "") {
                $("#fono-error").text("Por favor, ingrese un número de teléfono válido.");
                return;
            }
            if (!telefonoRegex.test(telefono)) {
                $("#fono-error").text("Por favor, ingrese solo números en el teléfono.");
                return;
            }

            
            if ($("#correo").val() === "") {
                $("#correo-error").text("Por favor, ingrese un correo electrónico válido.");
                return;
            }
            var correo = $("#correo").val();
            var correoRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            if (!correoRegex.test(correo)) {
                $("#correo-error").text("Por favor, ingrese un correo electrónico con formato válido.");
                return;
            }

            
            if ($("#mensaje").val() === "") {
                $("#mensaje-error").text("Por favor, ingrese un mensaje válido.");
                return;
            }

            
            $("#mensaje-exito").text("¡Mensaje enviado exitosamente!").show();  
            setTimeout(function () {
                this.submit(); 
            }.bind(this), 2000);  
        }

    
        else if (formulario === "formulario_registro") {
            
            var tipoUsuario = $("#tipo_usuario").val();
            if (tipoUsuario === "") {
                $("#tipo_usuario-error").text("Por favor, seleccione un tipo de usuario.");
                return;
            }

           
            var nombre = $("#nombre").val();
            var nombreRegex = /^[a-zA-ZáéíóúÁÉÍÓÚñÑ\s]+$/;
            if (nombre === "") {
                $("#nombre-error").text("Por favor, ingrese un nombre válido.");
                return;
            }
            if (!nombreRegex.test(nombre)) {
                $("#nombre-error").text("Por favor, ingrese solo letras en el nombre.");
                return;
            }

            
            if ($("#direccion").val() === "") {
                $("#direccion-error").text("Por favor, ingrese una dirección válida.");
                return;
            }

            
            var telefono = $("#fono").val();
            var telefonoRegex = /^[0-9]+$/;
            if (telefono === "") {
                $("#fono-error").text("Por favor, ingrese un número de teléfono válido.");
                return;
            }
            if (!telefonoRegex.test(telefono)) {
                $("#fono-error").text("Por favor, ingrese solo números en el teléfono.");
                return;
            }

            
            if ($("#correo").val() === "") {
                $("#correo-error").text("Por favor, ingrese un correo electrónico válido.");
                return;
            }
            var correo = $("#correo").val();
            var correoRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            if (!correoRegex.test(correo)) {
                $("#correo-error").text("Por favor, ingrese un correo electrónico con formato válido.");
                return;
            }

           
            if ($("#mensaje").val() === "") {
                $("#mensaje-error").text("Por favor, ingrese un mensaje válido.");
                return;
            }

            
            $("#mensaje-exito").text("¡Usuario registrado exitosamente!").show();  
            setTimeout(function () {
                this.submit(); 
            }.bind(this), 2000);  
        }

        
        else if (formulario === "formulario_login") {
            
            var correo = $("#correo").val();
            if (correo === "") {
                $("#correo-error").text("Por favor, ingrese un correo electrónico.");
                return;
            }
            var correoRegex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,6}$/;
            if (!correoRegex.test(correo)) {
                $("#correo-error").text("Por favor, ingrese un correo electrónico con formato válido.");
                return;
            }

           
            var contraseña = $("#mensaje").val();
            if (contraseña === "") {
                $("#mensaje-error").text("Por favor, ingrese una contraseña.");
                return;
            }

            
            $("#mensaje-exito").text("¡Inicio de sesión exitoso!").show();  
            setTimeout(function () {
                this.submit(); 
            }.bind(this), 2000);  
        }
    });
});


function agregarCompra(event) {
    
    event.preventDefault();

    
    var mensaje = document.createElement("p");
    mensaje.innerHTML = "Agregado a tu Carro de Compra"; 
    mensaje.style.color = "white";  

    
    var contenedor = document.getElementById("mensaje-container");

    
    contenedor.appendChild(mensaje);

    
    setTimeout(function() {
        mensaje.style.display = "none";  
    }, 2000);  
}

