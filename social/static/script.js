$(document).ready(function() {
  $('.carousel').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    dots: false,
    prevArrow: $('.carousel-prev'),
    nextArrow: $('.carousel-next')
  });
});
