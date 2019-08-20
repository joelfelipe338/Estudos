$(function(){
	$("li").hover(function(){
		$(this).find(".menu2").show('fast');
	},function(){
		$(this).find(".menu2").hide('fast');
	});
});