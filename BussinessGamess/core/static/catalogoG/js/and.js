$(document).ready(function() {
    $("[data-role='controlgroup']").on("change", function() {
        var csrftoken = getCookie('csrftoken');
        var videojuego = $("#formulario").attr("id_co");
        var radiobtns = $("input", this),
            Moment = "";
        radiobtns.each(function() {
            if ($(this).is(":checked")) {
                Moment = $(this).val();
            }

        });
        console.log(Moment)
        console.log(videojuego)
        $.ajax({
                type: "post",
                url: "/votacion/",
                data: {
                    videojuego: videojuego,
                    voto: Moment,
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
                alert(response.mensaje);

            });
    });

});


$(document).ready(function() {
    $('#botonenviar').on('click', function() {
        var csrftoken = getCookie('csrftoken');
        if (validaForm()) {
            var videojuego = $("#formulario").attr("id_co");
            var comentario = $("#exampleFormControlTextarea1").val()
            $('textarea[type="text"]').val('');
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
                    var html;
                    var imagen = "{% static 'pacho/assets/man.png' %}";
                    console.log(response);
                    //$("#comentario").prepend('<p class="commentText">' + response.text + '</p>');
                    html = '<div class="row commentsUsers align-items-center" >';
                    html += '<div class="col-md-2">';
                    html += '<div class="imgBox">'
                    html += '<img class="imgProfile" src="/static/pacho/assets/man_2.png">';
                    html += '</div>';
                    html += '</div>';
                    html += '<div class="col-md-10">';
                    html += '<p class="commentText">' + response.text + '</p>';
                    html += '</div>';
                    html += '</div>';

                    $('#comentario').prepend(html);

                });
        }
    });
});

function validaForm() {
    // Campos de texto
    if ($("#exampleFormControlTextarea1").val() == "") {
        alert("El campo no puede estar vacío.");
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

$(document).ready(function() {
    $('#button-addon2').on('click', function() {
        var busqueda = $("#inputBuscador").val()
        var url = "http://127.0.0.1:8000/general/?nombre=" + busqueda;
        $(location).attr('href', url);
        d = document.getElementById("borrado");
        while (d.hasChildNodes())
            d.removeChild(d.firstChild);
        if (busqueda != '') {
            $.ajax({
                    type: 'GET',
                    url: "/buscador",
                    data: {
                        busqueda: busqueda,
                    },
                    dataType: 'json',
                    cache: false

                })
                .done(function(response) {
                    var html = '';
                    console.log(response)
                    $.each(JSON.parse(response), function(index, element) {
                        cambio = element.id
                        console.log(cambio)
                        imagen = "/media/" + element.fields.image
                        html = '<div class="mainContent container-fluid >'
                        html += '<div class="row justify-content-center">'
                        html += '<div class="col-8">'
                            //html += '</div><div class="titleDiv">'
                            //html = '<img class="logo_login" src="/static/pacho/assets/bg_logo.png">'
                            //html = '<h1 class="welcome_text">Lo mas destacado de la semana</h1>'
                            //html += '</div></div>'
                        html += '<div class="vgSection">'
                        html += '<div class="row justify-content-center">'
                        html += '<div class="col-7">'
                        html += '<div class="vgCard">'
                        html += '<div class="container-fluid">'
                        html += '<div class="row align-items-center">'
                        html += '<div class="vgImage">'
                        html += '<img class="vgImg" src=' + imagen + '>'
                        html += '</div>'
                        html += '<div class="vgDetails">'
                        html += '<h3 class="vgTitle">' + element.fields.title + '</h3>'
                        html += '<div class="col-md-12 ">'
                        html += '<fieldset class="rating desktop-display-important pt-0">'
                        html += '<div class="vgImage ">'
                        html += '<img class="vgImg " src="/static/pacho/assets/star.png">'
                        html += '<div class="col-8"><h3  class="vgTitle">4.0</</h3></div>'
                        html += '</div>'
                        html += '</fieldset>'
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'
                        html += '</div>'

                        $('body').appendTo(html);



                    });
                });


        }

    });
});