/*
	Future Imperfect by HTML5 UP
	html5up.net | @ajlkn
	Free for personal and commercial use under the CCA 3.0 license (html5up.net/license)
*/
function judgeTerminalBrowser(userAgent) {
    let data = {
        terminal: undefined,
        browser: undefined
    };
    let regs = {};
    let terminal = {
        'android': 'Android',
        'iphone': 'iPhone',
        'windows nt 10': 'Windows 10',
        'windows nt 6.3': 'Windows 8.1',
        'windows nt 6.2': 'Windows 8',
        'windows nt 6.1': 'Windows 7',
        'windows nt 6.0': 'Windows Vista',
        'windows nt 5.2': 'Windows Server 2003XP x64',
        'windows nt 5.1': 'Windows XP',
        'windows xp': 'Windows XP',
        'windows nt 5.0': 'Windows 2000',
        'windows me': 'Windows ME',
        'win98': 'Windows 98',
        'win95': 'Windows 95',
        'win16': 'Windows 3.11',
        'macintosh|mac os x': 'Mac OS X',
        'mac_powerpc': 'Mac OS 9',
        'ubuntu': 'Ubuntu',
        'linux': 'Linux',
        'pod': 'iPod',
        'pad': 'iPad',
        'blackberry': 'BlackBerry',
        'webos': 'Mobile',
        'freebsd': 'FreeBSD',
        'sunos': 'Solaris'
    };

    for (let key in terminal) {
        if (new RegExp(key).test(userAgent.toLowerCase())) {
            data.terminal = terminal[key];
            break;
        }
    }

    if (regs = userAgent.match(/MSIE\s(\d+)\..*/)) {
        // ie 除11
        data.browser = 'ie ' + regs['1'];
    } else if (regs = userAgent.match(/FireFox\/(\d+)\..*/)) {
        data.browser = 'firefox ' + regs['1'];
    } else if (regs = userAgent.match(/Opera[\s|\/](\d+)\..*/)) {
        data.browser = 'opera ' + regs['1'];
    } else if (regs = userAgent.match(/Edge[\s|\/](\d+)\..*/)) {
        data.browser = 'edge ' + regs['1'];
    } else if (regs = userAgent.match(/Chrome\/(\d+)\..*/)) {
        data.browser = 'chrome ' + regs['1'];
    } else if (regs = userAgent.match(/Safari\/(\d+)\..*$/)) {
        // chrome浏览器都声明了safari
        data.browser = 'safari ' + regs['1'];
    } else if (regs = userAgent.match(/rv:(\d+)\..*/)) {
        // ie 11
        data.browser = 'ie ' + regs['1'];
    }

    return data;
}


function getReferrer() {
    var referrer = '';
    try {
        referrer = window.top.document.referrer;
    } catch (e) {
        if (window.parent) {
            try {
                referrer = window.parent.document.referrer;
            } catch (e2) {
                referrer = '';
            }
        }
    }
    // finally {
    //     if (referrer === '') {
    //         referrer = document.referrer;
    //     }
    //
    // }
    return referrer;

}

(function ($) {
        var second = 0;
        window.setInterval(function () {
            second++;
        }, 1000);
        var tjArr = undefined;
        // var tjArr = localStorage.getItem("jsArr") ? localStorage.getItem("jsArr") : '[{}]';
        // alert(tjArr);
        // $.cookie('tjRefer', getReferrer(), {expires: 1, path: '/'});
        window.onbeforeunload = function () {
            // if ($.cookie('tjRefer') == '') {
            //     var tjT = eval('(' + localStorage.getItem("jsArr") + ')');
            //     if (tjT) {
            //         tjT[tjT.length - 1].time += second;
            //         tjT[tjT.length - 1].refer = '';
            //         var jsArr = JSON.stringify(tjT);
            //         localStorage.clear();
            //         localStorage.setItem("jsArr", jsArr);
            //     }
            // } else {
            //     {
                    var dataArr = {
                        'url': location.href,
                        'time': second,
                        'refer': getReferrer(),
                        'timeIn': Date.parse(new Date()),
                        'timeOut': Date.parse(new Date()) + (second * 1000),
                    };
                    tjArr = JSON.stringify(dataArr);
                    // localStorage.clear();
                    // localStorage.setItem("jsArr", tjArr);
                // }
            // }
            $.ajax({
            'url': '/viewscount.html',
            'data': {
                data: JSON.stringify({
                    'ip': returnCitySN["cip"],
                    'address': returnCitySN["cname"],
                    'user_agent': JSON.stringify(judgeTerminalBrowser(navigator.userAgent)),
                    'tjArr': tjArr,
                })
            },
            'async' : false,
            'type': 'post',
            'dataType': 'json',
            'success': function (rs) {
                if (rs.status === 'ok') {
                    return true;
                } else {
                    alert(rs.content);
                    return false;
                }
            }
        });
        };


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
        });
    }
)(jQuery);