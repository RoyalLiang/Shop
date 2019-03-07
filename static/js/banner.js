(function () {
    img_len = 0;
    clock1 = undefined;
    now_img = img_len;
    var banner = function () {
        img_len = $(".img li").length;
        clock1 = undefined;
        now_img = img_len;
        for (var i = 0; i < img_len; i++) {
            $(".num").append($("<li>"))
        }
        $(".num li").mouseover(function () {
            var index = $(this).index();
            $(".num li").eq(index).addClass("active").siblings().removeClass("active");
            show(index);
            now_img = index;
        });
        $(".left").click(left1);
        $(".right").click(right);
        $(".outer").mouseover(function () {
            $(".left,.right").removeClass("hide");
            end()
        }).mouseout(function () {
            $(".left,.right").addClass("hide");
            start();
        });
        var left = ($(".outer").width() - $(".num").width()) / 2;
        $(".num").css("left", left + "px");
        right();
        start();
    };

    function show(index) {
        $(".img li").eq(index).stop().fadeIn(1000).siblings().stop().fadeOut(1000);
    }

    function right() {
        now_img++;
        if (now_img >= img_len)
            now_img = 0;
        show(now_img);
        $(".num li").eq(now_img).addClass("active").siblings().removeClass("active");
    }

    function left1() {
        now_img--;
        if (now_img < 0)
            now_img = img_len - 1;
        show(now_img);
        $(".num li").eq(now_img).addClass("active").siblings().removeClass("active");

    }

    function start() {
        clock1 = setInterval(right, 3000)
    }

    function end() {
        clearInterval(clock1);
        clock1 = undefined;
    }

    window.banner = banner;
}());