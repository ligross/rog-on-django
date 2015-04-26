$(function() {
    var url = window.location;

// Will only work if string in href matches with location
    $('nav.li a[href="' + url.pathname + '"]').parent().addClass('active');

// Will also work for relative and absolute hrefs
    $('nav.li a').filter(function () {
        return this.href == url.pathname;
    }).parent().addClass('active');
// hide #back-top first
    $("#back-top").hide();
})

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