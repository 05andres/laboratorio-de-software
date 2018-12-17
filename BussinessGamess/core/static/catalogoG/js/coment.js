$(document).ready(function() {
    var data = $("#formulario").attr("id_co");
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
                console.log("hola")
                var imagen = "{% static 'pacho/assets/man.png' %}";
                $.each(JSON.parse(response), function(index, element) {
                    //you can also use a templating engine like Underscore.js (the one I use), Mustache.js, Handlebars.js  http://garann.github.io/template-chooser/
                    //html = '<li><strong>' + element.fields.text + '</strong> - <em> ' + element.fields.owner_username + '</em> - <span> ' + element.fields.created + '</span></li>';
                    html = '<div class="row commentsUsers align-items-center" >';
                    html += '<div class="col-md-2">';
                    html += '<div class="imgBox">'
                    html += '<img class="imgProfile" src="/static/pacho/assets/man_2.png">';
                    html += '</div>';
                    html += '</div>';
                    html += '<div class="col-md-10">';
                    html += '<p class="commentText">' + element.fields.text + '</p>';
                    html += '</div>';
                    html += '</div>';

                    $('.commentsUsersRow').append(html);
                });


            });
    };
});

function comprar() {
    var user = $("#botoncompra").attr("id_user2");
    var videojuego = $("#botoncompra").attr("video");
    var video = videojuego.split(" ")
    console.log(user, videojuego);
    var csrftoken = getCookie('csrftoken');
    $.ajax({
            type: "post",
            url: "/venta/",
            data: {
                usuario: user,
                video: videojuego,
                csrfmiddlewaretoken: csrftoken,

            },
            beforeSend: function(xhr, settings) {
                if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                    xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
            },
            dataType: 'json',
            cache: false,
            //success: function(data) {
            //console.log(data)}

        })
        .done(function(response) {
            alert(response.mensaje)
        });

};


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