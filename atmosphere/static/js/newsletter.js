$(document).ajaxSend(function(event, xhr, settings) {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    function sameOrigin(url) {
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }
    function safeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    }
});
(function (){
    $(document).ready(function(){
          $("#form_subscribe").submit(function(e){
            e.preventDefault();
            console.log('index')
            subscribe_newsletter();
            });
          $('#footer_newsletter').submit(function(e){
            e.preventDefault();
            console.log('footer');
            subscribe_newsletter();
          });

    function subscribe_newsletter(){
            var $inputs = $(this).children('input');
            var values = {};
            var url = $(this).attr('action');
            $inputs.each(function(i,el) {
              values[el.name] = $(el).val();
            });
            values['email'] = $('.id_email').val();
            $('body').prepend('<div id="loader"><img src="'+STATIC_URL+'img/loading.gif" alt="" /></div>');
            $.ajax({
                data: values,
                dataType: 'json',
                type: 'POST',
                url: url,
                complete: function(){
                    $('#loader').fadeOut();
                },
                success:function(data){
                    if (data == 'inscri') {
                        $('#newsmodal p').html(gettext("Votre inscription a bien été pris en compte. Un email vous a été envoyé pour confirmer l'inscription"))
                        $('#newsmodal').modal('show');
                    }
                    else if(data == 'already') {
                        $('#newsmodal p').html(gettext('Votre email est déjà inscrit à la newsletter. Veuillez en choisir un autre'));
                        $('#newsmodal').modal('show');
                    }
                    else if(data == 'incorrect'){
                        $('#newsmodal p').html(gettext('Votre email est invalide'));
                        $('#newsmodal').modal('show');
                    }
                },
            });
    }
    });
})();
