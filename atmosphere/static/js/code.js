
$(document).ready(function(){


//On affiche la flèche uniquement si l'élément parent contient un sous-emnu

	var sousMenu = $('.s-menu');
	if (sousMenu) {
		 $('.main-nav > li .s-menu').parent().addClass('show-arrow');
	};


	$('.main-slider-container .slides-list').bxSlider({
	  infiniteLoop: true,
	  nextSelector: '.main-slider-container .slider-arrows.next',
	  prevSelector: '.main-slider-container .slider-arrows.prev',
	  nextText: '<span class="display">Suivant</span>',
	  prevText: '<span class="display">Prédédent</span>',
	  captions: true,
	  auto: true,
	});


	$('.hp-article-list').bxSlider({
	  infiniteLoop: false,
	  nextSelector: '.hp-articles-container .slider-arrow.next',
	  prevSelector: '.hp-articles-container .slider-arrow.prev',
	  nextText: '<span class="display">Suivant</span>',
	  prevText: '<span class="display">Prédédent</span>',
	  captions: false
	});


	$('.footer-slider-container .slides-list').bxSlider({
	  infiniteLoop: false,
	  nextSelector: '.footer-slider-container .slider-arrow.next',
	  prevSelector: '.footer-slider-container .slider-arrow.prev',
	  nextText: '<span class="display">Suivant</span>',
	  prevText: '<span class="display">Prédédent</span>',
	  captions: false,
	  maxSlides: 4,
	  moveSlides: 1,
	  slideWidth: 215
	});





});
