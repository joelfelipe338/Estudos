$(function(){
	$("button").bind("click",function(){
		var altura = parseFloat(($("input").eq(0).val())/100);
		var peso = parseFloat($("input").eq(1).val());
		var imc = peso/(altura*altura);
		if(imc < 18.5){
			var text = "seu IMC é " + imc.toFixed(2) + "kg/m² e seu status é: Abaixo do Peso";
			$("#resultado").html(text);
		}else if(imc >= 18.5 && imc < 25){
			var text = "seu IMC é " + imc.toFixed(2) + "kg/m² e seu status é: Peso Normal";
			$("#resultado").html(text);
		}else if(imc >= 25 && imc < 30){
			var text = "seu IMC é " + imc.toFixed(2) + "kg/m² e seu status é: Sobrepeso";
			$("#resultado").html(text);
		}else if(imc >= 30 && imc < 35){
			var text = "seu IMC é " + imc.toFixed(2) + "kg/m² e seu status é: Obesidade grau 1";
			$("#resultado").html(text);
		}else if(imc >= 35 && imc < 40){
			var text = "seu IMC é " + imc.toFixed(2) + "kg/m² e seu status é: Obesidade grau 2";
			$("#resultado").html(text);
		}else{
			var text = "seu IMC é " + imc.toFixed(2) + "kg/m² e seu status é: Obesidade grau 3";
			$("#resultado").html(text);
		}
	});
});

