$(document).ready(function() {
    var data = $("#formulario").attr("id_co");
    console.log(data)
    actualizar();

    function actualizar() {
        $.ajax({
                type: "GET",
                url: "/lista_comentarios",
                data: {
                    co_id: data
                },
                dataType: 'json',
                contentType: 'application/json',
                cache: false,
                //success: function(data) {
                //console.log(data)}

            })
            .done(function(response) {
                console.log(response);
                var html;
                $.each(JSON.parse(response), function(index, element) {
                    //you can also use a templating engine like Underscore.js (the one I use), Mustache.js, Handlebars.js  http://garann.github.io/template-chooser/
                    html = '<li><strong>' + element.fields.text + '</strong> - <em> ' + element.fields.owner_username + '</em> - <span> ' + element.fields.created + '</span></li>';

                    $('body').append(html);
                });


            });
    };
});



$(document).ready(function() {
    $('#botonenviar').on('click', function() {
        var csrftoken = getCookie('csrftoken');
        if (validaForm()) {
            var videojuego = $("#formulario").attr("id_co");
            var comentario = $("#nombre").val()
            $('input[type="text"]').val('');
            console.log(comentario)
            console.log(videojuego)
            $.ajax({
                    type: "post",
                    url: "/comentarBDD/",
                    data: {
                        videojuego: videojuego,
                        comentario: comentario,
                        csrfmiddlewaretoken: csrftoken,

                    },

                    beforeSend: function(xhr, settings) {
                        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                            xhr.setRequestHeader("X-CSRFToken", csrftoken);
                        }
                    },
                    dataType: 'json',
                    cache: false

                })
                .done(function(response) {
                    console.log(response);
                    $("#comentario").prepend("<li><strong>" + response.text + " </strong> - <em>" + response.nombre + "</em> </li>");

                });
        }
    });
});

function validaForm() {
    // Campos de texto
    if ($("#nombre").val() == "") {
        alert("El campo Nombre no puede estar vacío.");
        $("#nombre").focus(); // Esta función coloca el foco de escritura del usuario en el campo Nombre directamente.
        return false;
    }
    return true; // Si todo está correcto
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