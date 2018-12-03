var evitar = 1;

function descuentos() {
    if (evitar == 1) {
        var html;
        html = '-<em><h5 class="vgDetailText">Valor del descuento en % </h5><strong> <input id="descu" class=valor type="number" name="fname"  required="required"><input  type="button" onclick="asignar()" name="fname"  value="realizar descuentos"  ><br></br>';
        $('#formdataa').append(html);
        evitar = 0;
    }
}

function validaForm() {
    // Campos de texto
    if ($("#descu").val() == "") {
        alert("El campo no puede estar vacío.");
        $("#descu").focus(); // Esta función coloca el foco de escritura del usuario en el campo Nombre directamente.
        return false;

    }
    if ($("#descu").val() < 0) {
        alert("no puede ser negativo");
        $("#descu").focus(); // Esta función coloca el foco de escritura del usuario en el campo Nombre directamente.
        return false;
    }
    return true; // Si todo está correcto
}

function asignar() {
    if (validaForm()) {
        var csrftoken = getCookie('csrftoken');
        var videojuego = $("#formdata").attr("id_co");
        var precio = $("#formdata").attr("id_valor");
        var descuento = $("#descu").val();
        console.log(videojuego);
        console.log(descuento);
        console.log(precio);
        $("#descu").val("");
        $.ajax({
                type: "post",
                url: "/descuentos/",
                data: {
                    videojuego: videojuego,
                    precio: precio,
                    descuento: descuento,
                    csrfmiddlewaretoken: csrftoken,
                },
                /*beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                },*/
                dataType: 'json',
                cache: false

            })
            .done(function(response) {

                console.log(response);
                alert(response.mensaje);

            });

    }
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}