(function ($) {
  "user strict";
  // Preloader Js
  $(window).on('load', function () {
    $("[data-paroller-factor]").paroller();
    $('.preloader').fadeOut(1000);
    var img = $('.bg_img');
    img.css('background-image', function () {
      var bg = ('url(' + $(this).data('background') + ')');
      return bg;
    });
  });
  $(document).ready(function () {
    // Nice Select
    $('.select-bar').niceSelect();
    // PoPuP 
    $('.popup').magnificPopup({
      disableOn: 700,
      type: 'iframe',
      mainClass: 'mfp-fade',
      removalDelay: 160,
      preloader: false,
      fixedContentPos: false,
      disableOn: 300
    });
    $("body").each(function () {
      $(this).find(".img-pop").magnificPopup({
        type: "image",
        gallery: {
          enabled: true
        }
      });
    });
    // aos js active
    new WOW().init()
    //Faq
    $('.faq-wrapper .faq-title').on('click', function (e) {
      var element = $(this).parent('.faq-item');
      if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('.faq-content').removeClass('open');
        element.find('.faq-content').slideUp(300, "swing");
      } else {
        element.addClass('open');
        element.children('.faq-content').slideDown(300, "swing");
        element.siblings('.faq-item').children('.faq-content').slideUp(300, "swing");
        element.siblings('.faq-item').removeClass('open');
        element.siblings('.faq-item').find('.faq-title').removeClass('open');
        element.siblings('.faq-item').find('.faq-content').slideUp(300, "swing");
      }
    });
    $('.category-list .category-title').on('click', function (e) {
      var elementT = $(this).parent('.category-item');
      if (elementT.hasClass('open')) {
        elementT.removeClass('open');
        elementT.find('.category-content').removeClass('open');
        elementT.find('.category-content').slideUp(300, "swing");
      } else {
        elementT.addClass('open');
        elementT.children('.category-content').slideDown(300, "swing");
        elementT.siblings('.category-item').children('category-title').slideUp(300, "swing");
        elementT.siblings('.category-item').removeClass('open');
        elementT.siblings('.category-item').find('category-title').removeClass('open');
        elementT.siblings('.category-item').find('.category-content').slideUp(300, "swing");
      }
    });
    //Menu Dropdown Icon Adding
    $("ul>li>.submenu").parent("li").addClass("menu-item-has-children");
    // drop down menu width overflow problem fix
    $('ul').parent('li').hover(function () {
      var menu = $(this).find("ul");
      var menupos = $(menu).offset();
      if (menupos.left + menu.width() > $(window).width()) {
        var newpos = -$(menu).width();
        menu.css({
          left: newpos
        });
      }
    });
    $('.menu li a').on('click', function (e) {
      var element = $(this).parent('li');
      if (element.hasClass('open')) {
        element.removeClass('open');
        element.find('li').removeClass('open');
        element.find('ul').slideUp(300, "swing");
      } else {
        element.addClass('open');
        element.children('ul').slideDown(300, "swing");
        element.siblings('li').children('ul').slideUp(300, "swing");
        element.siblings('li').removeClass('open');
        element.siblings('li').find('li').removeClass('open');
        element.siblings('li').find('ul').slideUp(300, "swing");
      }
    })
    // Scroll To Top 
    var scrollTop = $(".scrollToTop");
    $(window).on('scroll', function () {
      if ($(this).scrollTop() < 500) {
        scrollTop.removeClass("active");
      } else {
        scrollTop.addClass("active");
      }
    });
    //Click event to scroll to top
    $('.scrollToTop').on('click', function () {
      $('html, body').animate({
        scrollTop: 0
      }, 500);
      return false;
    });
    //Header Bar
    $('.header-bar').on('click', function () {
      $(this).toggleClass('active');
      $('.overlay').toggleClass('active');
      $('.menu').toggleClass('active');
    })
    //Header Bar
    $('.overlay').on('click', function () {
      $(this).removeClass('active');
      $('.header-bar').removeClass('active');
      $('.menu').removeClass('active');
    })
    // Header Sticky Herevar prevScrollpos = window.pageYOffset;
    var scrollPosition = window.scrollY;
    if (scrollPosition >= 1) {
      $(".header-section").addClass('active');
    }
    var fixed_top_three = $(".header-section");
    $(window).on('scroll', function () {
      if ($(this).scrollTop() < 1) {
        fixed_top_three.removeClass("active");
      } else {
        fixed_top_three.addClass("active");
      }
    });
    //Tab Section
    // $('.tab ul.tab-menu').addClass('active').find('> li:eq(0)').addClass('active');
    $('.tab ul.tab-menu li').on('click', function (g) {
      var tab = $(this).closest('.tab'),
        index = $(this).closest('li').index();
      tab.find('li').siblings('li').removeClass('active');
      $(this).closest('li').addClass('active');
      tab.find('.tab-area').find('div.tab-item').not('div.tab-item:eq(' + index + ')').hide(10);
      tab.find('.tab-area').find('div.tab-item:eq(' + index + ')').fadeIn(10);
      g.preventDefault();
    });
    //Odometer
    $(".counter-item").each(function () {
      $(this).isInViewport(function (status) {
        if (status === "entered") {
          for (var i = 0; i < document.querySelectorAll(".odometer").length; i++) {
            var el = document.querySelectorAll('.odometer')[i];
            el.innerHTML = el.getAttribute("data-odometer-final");
          }
        }
      });
    }); //client slider
    var swiper = new Swiper('.feature-slider', {
      slidesPerView: 3,
      loop: true,
      breakpoints: {
          991: {
            slidesPerView: 2,
          },
          767: {
            slidesPerView: 1,
          },
      },
      speed: 300,
      loop: true,
      autoplay: {
          delay: 2500,
          disableOnInteraction: true,
      },
    });
    var swiper = new Swiper('.ticket-slider', {
      slidesPerView: 3,
      loop: true,
      spaceBetween: 30,
      breakpoints: {
          991: {
            slidesPerView: 2,
          },
          767: {
            slidesPerView: 1,
          },
      },
      speed: 300,
      loop: true,
      autoplay: {
          delay: 2500,
          disableOnInteraction: true,
      },
    }); 
    var swiper = new Swiper('.client-slider', {
      grabCursor: true,
      loop: true,
      effect: 'flip',
      navigation: {
        nextEl: '.client-next',
        prevEl: '.client-prev',
      },
      autoplay: {
        delay: 2000,
        disableOnInteraction: true,
      },
      breakpoints: {
        576: {
          pagination: false,
        },
      },
    });
    var swiper = new Swiper('.client--slider', {
      grabCursor: true,
      loop: true,
      autoplay: {
        delay: 2000,
        disableOnInteraction: true,
      },
      breakpoints: {
        576: {
          pagination: false,
        },
      },
    });
    $('.tab-in').on('click', function() {
      $('.trigon-5').addClass('active')
    })
    $('.tab-out').on('click', function() {
      $('.trigon-5').removeClass('active')
    })
    
    var elem = document.getElementById("myScreen");
    var elemBtn = document.getElementById("fullScreen");
    $(elemBtn).on('click', function() {
      if (elem.requestFullscreen) {
        elem.requestFullscreen();
      } else if (elem.mozRequestFullScreen) {
        elem.mozRequestFullScreen();
      } else if (elem.webkitRequestFullscreen) {
        elem.webkitRequestFullscreen();
      } else if (elem.msRequestFullscreen) {
        elem.msRequestFullscreen();
      }
    })
    var elemBtnTwo = document.getElementById("exitScreen");
    $(elemBtnTwo).on('click', function() {
      if (document.exitFullscreen) {
        document.exitFullscreen();
      } else if (document.mozCancelFullScreen) {
        document.mozCancelFullScreen();
      } else if (document.webkitExitFullscreen) {
        document.webkitExitFullscreen();
      } else if (document.msExitFullscreen) {
        document.msExitFullscreen();
      }
    })
    // Log OUt
    $('.log-out').on('click', function () {
      $('.log-out-option').toggleClass('active')
    })
  });
})(jQuery);
