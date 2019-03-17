/*
	Future Imperfect by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/

(function ($) {

    var $window = $(window),
        $body = $('body'),
        $menu = $('#menu'),
        $sidebar = $('#sidebar'),
        $main = $('#main');

    // Breakpoints.
    breakpoints({
        xlarge: ['1281px', '1680px'],
        large: ['981px', '1280px'],
        medium: ['737px', '980px'],
        small: ['481px', '736px'],
        xsmall: [null, '480px']
    });

    // Play initial animations on page load.
    $window.on('load', function () {
        window.setTimeout(function () {
            $body.removeClass('is-preload');
        }, 100);
    });

    // Menu.
    $menu
        .appendTo($body)
        .panel({
            delay: 500,
            hideOnClick: true,
            hideOnSwipe: true,
            resetScroll: true,
            resetForms: true,
            side: 'right',
            target: $body,
            visibleClass: 'is-menu-visible'
        });

    // Search (header).
    var $search = $('#search'),
        $search_input = $search.find('input');

    $body
        .on('click', '[href="#search"]', function (event) {

            event.preventDefault();

            // Not visible?
            if (!$search.hasClass('visible')) {

                // Reset form.
                $search[0].reset();

                // Show.
                $search.addClass('visible');

                // Focus input.
                $search_input.focus();

            }

        });

    $search_input
        .on('keydown', function (event) {

            if (event.keyCode == 27)
                $search_input.blur();

        })
        .on('blur', function () {
            window.setTimeout(function () {
                $search.removeClass('visible');
            }, 100);
        });

    // Intro.
    var $intro = $('#intro');

    // Move to main on <=large, back to sidebar on >large.
    breakpoints.on('<=large', function () {
        $intro.prependTo($main);
    });

    breakpoints.on('>large', function () {
        $intro.prependTo($sidebar);
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            var csrftoken = getCookie('csrftoken');
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    })
    ;


    $.ajax({
        'url': '/viewscount.html?t=' + new Date().getTime(),
        'data': {
            'cip': returnCitySN["cip"],
            'cname': returnCitySN["cname"],
        },
        'type': 'post',
        'dataType': 'json',
        'success': function (rs) {
            if (rs.status === 'ok') {
                alert('ok');
            } else {
                alert(rs.content);
                return false;
            }
        }
    });


})(jQuery);