$(document).ready(function(){
    var wh = $(window).height();
    var ww = $(window).width();
    if (wh>=ww){
        $('.slide').height(ww);
    } else {
        $('.slide').height(ww/16*10);
    }
    
});