
(function() {

	// Vars.
		var	window = (window),
			body = ('body'),
			wrapper = ('#wrapper');

	// Breakpoints.
		skel.breakpoints({
			xlarge:	'(max-width: 1680px)',
			large:	'(max-width: 1280px)',
			medium:	'(max-width: 980px)',
			small:	'(max-width: 736px)',
			xsmall:	'(max-width: 480px)'
		});

	// Disable animations/transitions until everything's loaded.
		body.addClass('is-loading');

		window.on('load', function() {
			body.removeClass('is-loading');
		});

	// Poptrox.

    //Fade AOS
    AOS.init({
        duration: 1200,
    })
		

});