/* Project specific Javascript goes here. */


// Side-nav Animation
$(function(){
	$('.side-nav-hover').hover(function(){
		$('#side-nav').css('transform', 'translate(0, 0)');
		// $(this).css('background-color', 'red');
	})

	var side_nav_container_width = $('.side-nav-container').innerWidth();
	console.log(side_nav_container_width);

	$('#side-nav').mouseleave(function(){
		$(this).css('transform', 'translate(-85%, 0)');
	})
});
