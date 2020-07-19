var $item = $('.carousel-item'); 
var $wHeight = $(window).height();
$item.eq(0).addClass('active');
$item.height($wHeight); 
$item.addClass('full-screen');

$('.carousel img').each(function() {
  var $src = $(this).attr('src');
  var $color = $(this).attr('data-color');
  $(this).parent().css({
    'background-image' : 'url(' + $src + ')',
    'background-color' : $color,
    // 'background-size' : 'contain'
  });
  $(this).remove();
});

$(window).on('resize', function (){
  $wHeight = $(window).height();
  $item.height($wHeight);
});

$('.carousel').carousel({
  interval: 6000,
  pause: "false"
});

$(document).ready(function() {
 
  $("#custom-carousel").owlCarousel({
      loop: true,
      nav: true,
      dots : false,
      autoPlay: 3000, //Set AutoPlay to 3 seconds
 
      items : 4,
      itemsDesktop : [1199,3],
      itemsDesktopSmall : [979,3]
 
  });

  $("#custom-retaurant-carousel").owlCarousel({
    loop: true,
    nav: true,
    dots : false,
    autoPlay: 3000, //Set AutoPlay to 3 seconds

    items : 5,
    itemsDesktop : [1199,3],
    itemsDesktopSmall : [979,3]

});
 
});