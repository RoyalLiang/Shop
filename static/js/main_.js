/**
 * 通用模块
 *
 */

var $win = $(window),
    winW = $win.width(),
    $doc = $(document),
    $body = $('body', $doc),
    $header = $('.header', $body),
    $footer = $('.footer', $body),
    jNav = $('.navigation', $body);


/**
 * 图片加载
 */
$(function () {
    if (!$.fn.lazyload) return;
    $("img.lazy", $body).lazyload({
        effect: "fadeIn",
        threshold: 200
    });
});

$(function () {
    $(".nav").on("mouseenter", ".item", function (event) {
        if (winW < 992) return;
        $(this).children(".level-2").stop().fadeIn();
    }).on("mouseleave", "li", function (event) {
        if (winW < 992) return;
        $(this).children(".level-2").stop().fadeOut();
    });

    $(".level-2").on("mouseenter", "li", function (event) {
        if (winW < 992) return;
        $(this).children(".level-3").stop().fadeIn();
    }).on("mouseleave", "li", function (event) {
        if (winW < 992) return;
        $(this).children(".level-3").stop().fadeOut();
    });
});


/**
 * 顶部导航
 */

$(function () {
    var jNav = $('.navigation', $header);

    $header.on('click', '.nav-open .search', function (event) {
        event.preventDefault();
        event.stopPropagation();
        jNav.hide();
        $header.removeClass('nav-open');


    });
    $header.on('click', '.search', function (event) {
        event.preventDefault();
        event.stopPropagation();
        $header.removeClass('nav-open');

        $('.searchbox', $header).slideToggle();
        $(".tsearch").focus();

    });

    $header.on('click', '.sclose', function (event) {
        $('.searchbox', $header).slideUp();

    });

    $header.on('click', '.toggle', function (event) {
        event.preventDefault();
        event.stopPropagation();

        $header.toggleClass('nav-open');
        $('.searchbox', $header).hide();

        if (!$header.hasClass('nav-open')) {
            jNav.slideUp();
        } else {
            $('.search-box').slideUp('fast');
            jNav.slideDown();
            $body.one('click', function (event) {
                $header.removeClass('nav-open');
                jNav.slideUp();
            });
        }
    });


    jNav.on('click', function (event) {
        event.stopPropagation();
        event.preventDefault();
    }).on('click', '.level-1 > li', function (event) {
        event.stopPropagation();

        var jThis = $(this);
        jThis.toggleClass('active').siblings('li').removeClass('active');
        if (jThis.hasClass('more')) {
            event.preventDefault();
        }

        jThis.siblings('li').find('ul').slideUp();
        jThis.children('ul').slideToggle();

    }).on('click', '.level-2 > li', function (event) {
        event.stopPropagation();

        var jThis = $(this);
        jThis.toggleClass('active').siblings('li').removeClass('active');
        if (jThis.hasClass('more')) {
            event.preventDefault();
        }

        jThis.siblings('li').find('ul').slideUp();
        jThis.children('ul').slideToggle();

    }).on('click', '.level-3 > li', function (event) {
        event.stopPropagation();

        var jThis = $(this);
        jThis.toggleClass('active').siblings('li').removeClass('active');
        if (jThis.hasClass('more')) {
            event.preventDefault();
        }

        jThis.siblings('li').find('ul').slideUp();
        jThis.children('ul').slideToggle();

    }).on('click', '.level-4 > li', function (event) {
        location.href = $(this).find('a').attr('href');
    }).find('.level-2,.level-3,.level-4').each(function (index, el) {
        if ($(el).children('li').length) {
            $(el).parent('li').addClass('more');
        }
    });
});


/**
 * 幻灯切换
 */
$(function () {
    if (!$.fn.owlCarousel) return;

    // 首页 banner
    $('#owl-index').owlCarousel({
        autoPlay: 5000,
        autoPlay: true,
        autoHeight: false,

        stopOnHover: true,
        lazyLoad: true,

        singleItem: true,
        slideSpeed: 300,
        autoPlay: true,
        navigation: true,
        navigationText: false,
        paginationSpeed: 400,
        transitionStyle: "fade",

        afterAction: function () {
        }
    });


    $('#owl-other').owlCarousel({
        navigation: true,
        navigationText: false,

        pagination: true,
        paginationSpeed: 400,

        slideSpeed: 400,
        singleItem: false,

        items: 3,
        itemsDesktop: [1199, 2],
        itemsDesktopSmall: [991, 2],
        itemsTablet: [768, 2],
        itemsTabletSmall: [480, 1],
        itemsMobile: [320, 1],

        autoPlay: 3000,
        autoPlay: true,
        lazyLoad: true,

        autoHeight: false,
        stopOnHover: true,
        rewindNav: true,


        afterInit: function () {
            if ($body.width() < 768) this.stop();
        }
    });

    $('#owl-carousel-pro').owlCarousel({
        navigation: true,
        navigationText: false,

        pagination: false,
        paginationSpeed: 400,

        slideSpeed: 300,
        singleItem: false,

        items: 4,
        itemsDesktop: [1170, 4],
        itemsDesktopSmall: [991, 3],
        itemsTablet: [768, 3],
        itemsTabletSmall: [480, 2],
        itemsMobile: [320, 1],

        autoPlay: 5500,
        autoPlay: true,
        lazyLoad: true,

        autoHeight: true,
        stopOnHover: true,
        rewindNav: false,

        afterInit: function () {
            if ($body.width() < 768) this.stop();
        }
    });

});


$(function () {
    $('.flexslider').flexslider({
        // pauseOnAction: false,
        pauseOnHover: true,
        // multipleKeyboard: true,
        // mousewheel: true,
        //reverse :true
        slideshow: false,
        directionNav: false,
        touch: true,
        //smoothHeight: true
        //randomize: true
    });
});

$(function () {

    var sync1 = $("#sync1");
    var sync2 = $("#sync2");

    sync1.owlCarousel({
        autoPlay: true,
        singleItem: true,
        slideSpeed: 1000,
        navigation: true,
        pagination: false,
        lazyLoad: true,
        afterAction: syncPosition,
        responsiveRefreshRate: 200,
    });

    sync2.owlCarousel({
        autoPlay: true,
        items: 5,
        itemsDesktop: [1200, 5],
        itemsDesktopSmall: [991, 5],
        itemsTablet: [767, 5],
        itemsMobile: [480, 5],
        pagination: false,
        lazyLoad: true,
        responsiveRefreshRate: 100,
        afterInit: function (el) {
            el.find(".owl-item").eq(0).addClass("synced");
        }
    });

    function syncPosition(el) {
        var current = this.currentItem;
        $("#sync2")
            .find(".owl-item")
            .removeClass("synced")
            .eq(current)
            .addClass("synced")
        if ($("#sync2").data("owlCarousel") !== undefined) {
            center(current)
        }

    }

    $("#sync2").on("hover", ".owl-item", function (e) {
        e.preventDefault();
        var number = $(this).data("owlItem");
        sync1.trigger("owl.goTo", number);
    });

    function center(number) {
        var sync2visible = sync2.data("owlCarousel").owl.visibleItems;

        var num = number;
        var found = false;
        for (var i in sync2visible) {
            if (num === sync2visible[i]) {
                var found = true;
            }
        }

        if (found === false) {
            if (num > sync2visible[sync2visible.length - 1]) {
                sync2.trigger("owl.goTo", num - sync2visible.length + 2)
            } else {
                if (num - 1 === -1) {
                    num = 0;
                }
                sync2.trigger("owl.goTo", num);
            }
        } else if (num === sync2visible[sync2visible.length - 1]) {
            sync2.trigger("owl.goTo", sync2visible[1])
        } else if (num === sync2visible[0]) {
            sync2.trigger("owl.goTo", num - 1)
        }
    }

});


// 浮动客服弹出二维码and缓冲回到顶部

$(function () {
    $('.online > .online-tel').hover(function () {
        $('.online-tel p').stop(true, true).fadeIn();
    }, function () {
        $('.online-tel p').stop(true, true).fadeOut();
    });
    $('.online > .online-wechat').hover(function () {
        $('.online-wechat img').stop(true, true).fadeIn();
    }, function () {
        $('.online-wechat img').stop(true, true).fadeOut();
    });
    $('#backtop,.backtop').click(function () {
        $("html, body").animate({
            scrollTop: 0
        }, 400);
    });
});

$(function () {
    $('.icon-online').click(function () {
        $('.online').toggleClass('active');
        $('.icon-online').toggleClass('icon');
    });
});


// 放大
$(function () {
    $("a[rel=fancybox-product]").fancybox({
        'overlayShow': true,
        'overlayColor': '#000',
        'overlayOpacity': 0.9,
        'opacity': 0.5,
        'transitionIn': 'elastic',
        'transitionOut': 'none',
        'titlePosition': 'over',
        'showCloseButton': false,
        'titleFormat': function (title, currentArray, currentIndex, currentOpts) {
            return '<span id="fancybox-title-over">' + (currentIndex + 1) + ' / ' + currentArray.length + (title.length ? ' &nbsp; ' + title : '') + ' </span>';
        }
    });
});


// 视频
$(function () {
    var $box = $(".video", $body);
    if (!$box.length) return;

    $box.on('click', '.video-box .play', function (event) {
        event.preventDefault();
        var me = $(this);

        var $iframe = me.next('.iframe'),
            url = $iframe.data('src');

        if ($win.width() > 1200) {
            $.fancybox.open([url], {
                type: 'iframe',
                padding: 10,
            });
        } else {
            var height = me.find('.img-responsive').length ? me.height() : $box.height();
            height = Math.max(height, 170);
            if (!$iframe.attr('src')) $iframe.attr('src', url);
            $iframe.height(height);
            $iframe.css('display', 'block');
            me.hide();
        }
    });
});


// 产品详情tab选项卡
$(function () {
    $('.box-product .pro-sort ul li').click(function () {
        var liindex = $('.box-product .pro-sort ul li').index(this);
        $(this).addClass('active').siblings().removeClass('active');
        $('.box-product .pro-sort .info').eq(liindex).show().siblings('.box-product .pro-sort .info').hide();
    }).eq(0).click();
});

// 数字滚动
$(function () {
    $('.counter').countUp();

});

// 瀑布流
jQuery(document).ready(function ($) {
    $(".waterfall").mpmansory({
        childrenClass: 'item', // default is a div
        columnClasses: 'padding', //add classes to items
        breakpoints: {
            lg: 4,
            md: 4,
            sm: 6,
            xs: 12
        },
        distributeBy: {
            order: false,
            height: false,
            attr: 'data-order',
            attrOrder: 'asc'
        }, //default distribute by order, options => order: true/false, height: true/false, attr => 'data-order', attrOrder=> 'asc'/'desc'
        onload: function (items) {
            //make somthing with items
        }
    });
});



$(function () {
    $('.feedback-form,.feedback-form-inquire').on('click', '.submit', function (event) {
        event.preventDefault();
        var jForm = $(event.delegateTarget),
            jThis = $(this);
        if (jThis.hasClass('disabled')) {
            // alert('正在提交，请稍后...');
            alert('please wait...');
            return;
        }

        var reg_email = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
        var data = {
            email: $('input[name="email"]', jForm).val().trim(),
            title: $('input[name="inquire"]', jForm).val().trim(),
            content: $('textarea[name="message"]', jForm).val().trim()
        };

        if (!data.email || !reg_email.test(data.email)) {
            alert('Please enter a valid email address');
            // alert('请输入一个有效的邮箱地址');
            $('input[name="email"]', jForm).focus();
            return false;
        } else if (!data.title) {
            alert('The title cannot be empty');
            // alert('请输入留言主题');
            $('input[name="inquire"]', jForm).focus();
            return false;
        } else if (!data.content) {
            alert('The message cannot be empty');
            // alert('请输入留言内容');
            $('textarea[name="message"]', jForm).focus();
            return false;
        }

        jThis.text($(this).data('text-b')).css({
            opacity: '.5'
        }).addClass('disabled');


        // event.preventDefault();
        // var data = $(this).serializeArray();
        // $.get(, data, function (data) {
        //  /*optional stuff to do after success */
        // }, 'json');


        var url = "/goods/message.html?c=cart&f=sendMessage&t=" + new Date().getTime();
        $('.feedback-form .col-xs-12 .send span').text('submit.....');
        $.ajax({
            'url': url,
            'data': jForm.serializeArray(),
            'type': 'post',
            'dataType': 'json',
            'success': function (rs) {
                jThis.text(jThis.data('text')).css({
                    opacity: '1'
                }).removeClass('disabled');
                if (rs.status === 'ok') {
                    alert('Your message has been posted, please wait patiently administrator audit, thank you for your submission');
                    // alert('您的留言已提交,请耐心等候管理员回复');
                    $('.feedback-form .col-xs-12 .send span').text('submit');
                    if (jForm.hasClass('feedback-form-inquire')) {
                        location.href = '/goods_detail/' + $('input[name=id]').val();
                    } else {
                        jForm.get(0).reset();
                    }
                } else {
                    alert(rs.content);
                    return false;
                }
            }
        });
        return false;
    });
});
