window.t266showvideo = function(recid) {
    $(document).ready(function() {
        var el = $('#coverCarry' + recid);
        var videourl = '';
        var youtubeid = $("#rec" + recid + " .t266__video-container").attr('data-content-popup-video-url-youtube');
        if (youtubeid > '') {
            videourl = 'https://www.youtube.com/embed/' + youtubeid
        }
        $("body").addClass("t266__overflow");
        $("#rec" + recid + " .t266__cover").addClass("t266__hidden");
        $("#rec" + recid + " .t266__video-container").removeClass("t266__hidden");
        $("#rec" + recid + " .t266__video-carier").html("<iframe id=\"youtubeiframe" + recid + "\" class=\"t266__iframe\" width=\"100%\" height=\"540\" src=\"" + videourl + "?autoplay=1\" frameborder=\"0\" allowfullscreen></iframe><a class=\"t266__close-link\" href=\"javascript:t266hidevideo('" + recid + "');\"><div class=\"t266__close\"></div></a>")
    })
}
window.t266hidevideo = function(recid) {
    $(document).ready(function() {
        $("body").removeClass("t266__overflow");
        $("#rec" + recid + " .t266__cover").removeClass("t266__hidden");
        $("#rec" + recid + " .t266__video-container").addClass("t266__hidden");
        $("#rec" + recid + " .t266__video-carier").html("<div class=\"t266__video-bg2\"></div>")
    })
}