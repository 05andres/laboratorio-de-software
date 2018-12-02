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