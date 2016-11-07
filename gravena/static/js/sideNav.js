$(function(){
  var side_nav = $('#side-nav');
  var side_nav_hover = $('.side-nav-hover');
  var side_nav_translate = parseInt($('.side-nav-container').innerWidth()) + 'px';


  side_nav_hover.click(function(){
    side_nav.toggleClass( 'side-nav-translate' );
  });

  setTimeout(function(){ side_nav.addClass( 'side-nav-translate' ) }, 1000);

});
