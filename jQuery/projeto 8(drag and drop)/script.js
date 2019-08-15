


$(function(){

	$(".bola").bind("mousedown",function(){
		$(this).bind("mousemove",function(e){
			var mouseX = e.originalEvent.pageX;
			var mouseY = e.originalEvent.pageY;
			$(this).css("left",mouseX-25);
			$(this).css("top",mouseY-25);
			
		})
	})

	$(".bola").bind("mouseup",function(){
		$(this).unbind("mousemove");
	})

});