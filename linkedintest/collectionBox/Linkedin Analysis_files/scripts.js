/*-----------------------------------------------------------------------------------

    Template Name: Lavaland Multipurpose  Landing Html5 Template
    Template URI: http://tf.itech-theme.com/lavaland-preview/
    Description: This is a Multipurpose Landing Html5 Template
    Author: cdibrandstudio
    Version: 1.0

-----------------------------------------------------------------------------------*/

(function ($) {
    "use strict";

    /*================================
    Add ScrollUp Btn
    ==================================*/
    $("body").append("<a class='scroll_to_top' href='#top'><img src='/images/icons8-chevron.png'></a>");
    $('body').attr('id', 'top');

    /*================================
    Preloader
    ==================================*/
    // var preloader = $('#preloader');
    // $(window).on('load', function () {
    //     preloader.fadeOut('slow', function () { $(this).remove(); });
    // });

    /*================================
    stickey Header
    ==================================*/
    $(window).on('scroll', function () {
        var scroll = $(window).scrollTop(),
            mainHeader = $('.header-area'),
            scroll_to_top = $('.scroll_to_top');
        // sticky menu
        if (scroll > 100) {
            mainHeader.addClass("sticky-menu");
        } else {
            mainHeader.removeClass("sticky-menu");
        }

        // scrolltop
        if (scroll > 100) {
            scroll_to_top.addClass("active");
        } else {
            scroll_to_top.removeClass("active");
        }
    });

    // /*================================
    // Humberger
    // ==================================*/
    // $('.humberger-btn').on('click', function () {
    //     $(this).toggleClass('opened');
    //     $('.offset-menu').toggleClass('show_hide_menu');
    // });

    // $('.offset-inner ul li a').on('click', function () {
    //     $('.offset-menu').removeClass('show_hide_menu');
    //     $('.humberger-btn').removeClass('opened');
    // });

    /*================================
    Smoth Scroll
    ==================================*/
    function smoothScrolling($links, $topGap) {
        var links = $links;
        var topGap = $topGap;

        links.on("click", function () {
            if (location.pathname.replace(/^\//, '') === this.pathname.replace(/^\//, '') && location.hostname === this.hostname) {
                var target = $(this.hash);
                target = target.length ? target : $("[name=" + this.hash.slice(1) + "]");
                if (target.length) {
                    $("html, body").animate({
                        scrollTop: target.offset().top - topGap
                    }, 1000, "easeInOutExpo");
                    return false;
                }
            }
            return false;
        });
    }
    var mainHeaderHeight = $('.header-area').innerHeight();
    $(window).on("load", function () {
        smoothScrolling($("a.take-me[href^='#']"), mainHeaderHeight);
        smoothScrolling($(".offset-inner ul li a[href^='#']"), mainHeaderHeight);
        smoothScrolling($("a.scrl_me_down[href^='#']"), mainHeaderHeight);
        smoothScrolling($(".main-menu nav ul li a[href^='#']"), mainHeaderHeight);
        smoothScrolling($("a.scroll_to_top[href^='#']"), 0);
    });

    /*================================
    Active current Li
    ==================================*/
    $(window).on("scroll", function () {
        activeMenuItem($("#nav_mobile_menu"));
    });

    //function for active menuitem
    function activeMenuItem($links) {
        var top = $(window).scrollTop(),
            windowHeight = $(window).height(),
            documentHeight = $(document).height(),
            cur_pos = top + 2,
            sections = $("section"),
            nav = $links,
            nav_height = nav.outerHeight(),
            home = nav.find(" > ul > li:first");

        sections.each(function () {
            var top = $(this).offset().top - mainHeaderHeight,
                bottom = top + $(this).outerHeight();

            if (cur_pos >= top && cur_pos <= bottom) {
                nav.find("> ul > li > a").parent().removeClass("active");
                nav.find("a[href='#" + $(this).attr('id') + "']").parent().addClass("active");
            } else if (cur_pos === 2) {
                nav.find("> ul > li > a").parent().removeClass("active");
                home.addClass("active");
            } else if ($(window).scrollTop() + windowHeight > documentHeight - 400) {
                nav.find("> ul > li > a").parent().removeClass("active");
            }
        });
    }

    /*================================
    Swiper slider Activation
    ==================================*/
    // classes-carousel
    // function classes_carousel() {
    //     var mySwiper = new Swiper('.classes-carousel', {
    //         speed: 400,
    //         loop: true,
    //         spaceBetween: 30,
    //         slidesPerView: 3,
    //         pagination: {
    //             el: '.swiper-pagination',
    //             clickable: true
    //         },
    //         // Responsive breakpoints
    //         breakpoints: {
    //             640: {
    //                 slidesPerView: 1,
    //                 spaceBetween: 30
    //             },
    //             1024: {
    //                 slidesPerView: 2,
    //                 spaceBetween: 10
    //             }
    //         }
    //     });
    // }
    // classes_carousel();

    // // testimonials-carousel
    // function testimonials_carousel() {
    //     var mySwiper = new Swiper('.testimonials-carousel', {
    //         speed: 400,
    //         loop: true,
    //         grabCursor: true,
    //         slidesPerView: 1,
    //         pagination: {
    //             el: '.swiper-pagination',
    //             clickable: true
    //         }
    //     });
    // }
    // testimonials_carousel();

    // // photography slider
    // function photography_slider() {
    //     var mySwiper = new Swiper('.photography-slider', {
    //         speed: 400,
    //         loop: true,
    //         parallax: true,
    //         grabCursor: true,
    //         slidesPerView: 1,
    //         // Navigation arrows
    //         navigation: {
    //             nextEl: '.ph-button-next',
    //             prevEl: '.ph-button-prev',
    //         },
    //         pagination: {
    //             el: '.ph-pagination',
    //             type: 'fraction',
    //         }

    //     });
    // }
    // photography_slider();

    // // screen slider
    // function screen_slides() {
    //     var mySwiper = new Swiper('.screen-slides', {
    //         speed: 400,
    //         loop: true,
    //         slidesPerView: 1,
    //         autoplay: {
    //             delay: 3000,
    //         }
    //     });
    // }
    // screen_slides();

    // // screenshot slider
    // function screenshot_carousel() {
    //     var mySwiper = new Swiper('.screenshot-carousel', {
    //         pagination: {
    //             el: '.screenshot-pagination',
    //             type: 'bullets',
    //             clickable: true,
    //         },
    //         autoplay: {
    //             delay: 3000,
    //         },
    //         speed: 1000,
    //         effect: 'coverflow',
    //         loop: true,
    //         centeredSlides: true,
    //         slidesPerView: 'auto',
    //         coverflowEffect: {
    //             rotate: 0,
    //             stretch: 80,
    //             depth: 200,
    //             modifier: 1,
    //             slideShadows: false,
    //         }
    //     });
    // }
    // screenshot_carousel();

})(jQuery);
