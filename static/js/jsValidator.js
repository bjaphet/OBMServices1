$(document).ready(function(){
    $('input').keyup(function(){
        let textSaisi=$(this).val();
        if(textSaisi ==""){
            if(!$(this).hasClass('is-invalid')){
                $(this).addClass('is-invalid');
            }
        }
        else{
            $(this).removerClass('is-invalid')
        }
    })
   
        });