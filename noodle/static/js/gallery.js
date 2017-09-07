$(document).ready(function(){
    var sp = 1;
    var count=4;


    function changePhoto(inc){
        var ni=sp;
        ni+=inc;
        if (ni>count){
            ni=1;
        }
        if (ni===0){
            ni=count;
        }

        $('#p'+sp).fadeOut(100);
        sp=ni;
        setTimeout(function(){
            $('#p'+sp).fadeIn(300);
        }, 105);
    }


    // Running the gallery
    $('#main').height($(window).height()*0.95-70);
    $('.photo').hide();
    $('#p1').show();


    // Event listeners
    $('.photo').on('click', function(){
        changePhoto(1);
    });

    $('body').keyup(function(e){
        if(e.keyCode == 32 || e.keyCode == 39 || e.keyCode == 40 ){
            changePhoto(1);
        }
        else if(e.keyCode == 37 || e.keyCode == 38){
            changePhoto(-1);
        }
    });

});