function addBola(){
	var x = Math.floor(Math.random()*800);
	var y = Math.floor(Math.random()*800);
	var bola = $('<div class="bola"></div>');
	bola.css('left',x+'px');
	bola.css('top',y+'px');

	bola.bind('click',function(){
		$(this).fadeOut('fast');
		placar++;
		$("#placar").text(placar);
		$(this).unbind("click");
	})
	$(document.body).append(bola);
}

var placar = 0;

$(function(){


	$('.jogo').bind('click',function(){
		setInterval(addBola,1000);
	})


});

