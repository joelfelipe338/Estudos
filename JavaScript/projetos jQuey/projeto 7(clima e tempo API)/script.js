

$(function(){
	
	$("#pesq").bind("click",function(){
		var cidade = $("#cidade").val();
		var now = new Date();
		var temp = 'https://query.yahooapis.com/v1/public/yql?format=json&rnd=' + now.getFullYear() + now.getMonth()+ now.getDay() + now.getHours()+'&diagnostics=true&callback=?&q=';temp += 'select * from weather.forecast where woeid in (select woeid from geo.places(1) where text="'+cidade+'")and u="c"';
		//yahoo recomendação

		$.ajax({
			type:'GET',
			url:encodeURI(temp),//yahoo recomendação
			dataType:'json',
			beforeSend:function(){
				$("#res").html("Carregando...");
			},
			success:function(data){
				//yahoo recomendação
				if(data != null && data.query !== null && data.query.results !== null && data.query.results.channel.description !== 'Yahoo! Weather Error'){
					var temperatura = data.query.results.channel.item.condition.temp;
					$("#res").html(temperatura+'° C');
				}
			},
			error:function(){
				$("#res").html("Error");
			}
		})

	})

});