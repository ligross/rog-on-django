function initTabs() {
    if (window.location.host.hash != ('' || undefined)) tabSwitch(window.location.hash);
    $('#content_articles').hide();
    $('#content_db').hide();
    $('#content_video').hide();
    $('#content_gallery').hide();
};

function tabSwitch(nb) {
    window.location.hash = nb;
    $('#tabs a').removeClass('active');
    $('div.tab-content').hide();
    $('#tab_' + nb).addClass('active');
    $('#content_' + nb).show();
};

$(function() { initTabs(); });

// hide #back-top first
$("#back-top").hide();

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