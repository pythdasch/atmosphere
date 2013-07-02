(function (){
    $(document).ready(function(){
          $("#form_subscribe").submit(function(e){
            e.preventDefault();
            var $inputs = $(this).children('input');
            var values = {};
            var url = $(this).attr('action');
            $inputs.each(function(i,el) {
              values[el.name] = $(el).val();
            });
            values['email'] = $('#id_email').val();
            $.ajax({
                data: values,
                dataType: 'json',
                type: 'POST',
                url: url,
                success:function(data){
                    if (data == 'inscri') {
                        $('#newsmodal p').html("Votre inscription a bien été pris en compte. Un email vous a été envoyé pour confirmer l'inscription")
                        $('#newsmodal').modal('show');
                    }
                    else if(data == 'already') {
                        $('#newsmodal p').html('Votre email est déjà inscrit à la newsletter. Veuillez en choisir un autre');
                        $('#newsmodal').modal('show');
                    }
                    else if(data == 'incorrect'){
                        $('#newsmodal p').html('Votre email est invalide');
                        $('#newsmodal').modal('show');
                    }
                },
            });
     });
    });
})();