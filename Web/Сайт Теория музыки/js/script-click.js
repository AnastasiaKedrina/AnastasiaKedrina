jQuery(document).ready(function ($) {
    $('.button').on('click', function (e) {
        e.preventDefault();
        var
            href = $(this).attr('href'),
            timeout = 1000;

        setTimeout(function () {
            location.href = href;
        }, timeout);
    });
}); 