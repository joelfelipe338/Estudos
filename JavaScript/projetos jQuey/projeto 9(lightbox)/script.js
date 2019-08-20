$(function(){
	
	$(".galeria").bind("click",function(){
		var img = $(this).find("img").attr('src');
		$(".divbox img").attr("src",img);
		$(".divbox, .bgbox").fadeIn("fast");
	});


	$(".bgbox, .divbox button").bind("click",function(){
		$(".bgbox, .divbox").fadeOut("fast");
	});
});