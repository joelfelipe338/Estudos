$(function(){
	var campo;
	$("input").bind("focus",function(){

		var pos = $(this).offset();
		var width = $(this).width() + 5;

		$(".horaescolha").css("left",pos.left + width);
		$(".horaescolha").css("top",pos.top);
		$(".horaescolha").show();

		campo = $(this);

	});

	$("input").bind("blur",function(){
		setTimeout(function(){
			$(".horaescolha").hide();
		},200);
	});

	$("button").bind("click",function(){
		var hora = $(this).text();
		campo.val(hora);
	});

});