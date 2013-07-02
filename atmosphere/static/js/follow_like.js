(function (){
    $(document).ready(function(){
        $('#submit_subscribe').click(function(e){
            e.preventDefault();
            var btn = $(this);
            $.getJSON($('#form_subscribe').attr('action'), function (data){
                console.log(data);
            })
        });
     });
})();