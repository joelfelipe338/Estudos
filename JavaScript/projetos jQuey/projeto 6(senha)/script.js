


$(function(){
	
	$("#senha").bind('keyup',function(){
		var text = $(this).val();
		var forca = 0;

		//letra
		var reg = new RegExp(/[a-z]/i);
		if(reg.test(text)){
			forca += 25;
		}

		//numero
		var reg = new RegExp(/[0-9]/i);
		if(reg.test(text)){
			forca += 25;
		}
		//caracteres especiais
		var reg = new RegExp(/[^a-z0-9]/i);
		if(reg.test(text)){
			forca += 25;
		}
		//minimo
		if(text.length > 6){
			forca += 25;
		}

		if(forca >= 75){
			var aceita = 'ACEITA';
		}else{
			var aceita = 'NÃO ACEITA';
		}
		$('#forca').html('Força: '+forca+'% '+aceita);

	})

});