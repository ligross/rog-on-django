$(function() {
    var url = window.location;
    $('#categories a[href="' + url.pathname + '"]').parent().addClass('active');

});

// fade in #back-top
$(window).scroll(function () {
    if ($(this).scrollTop() > 100) {
        $('#back-top').fadeIn();
    } else {
        $('#back-top').fadeOut();
    }
});

// scroll body to 0px on click
function scroll () {
    $('body,html').animate({
        scrollTop: 0
    });
    return false;
};