var jogo = [0,0,0,0,0,0,0,0,0];
var clicou = 0;
function teste(){
	$("span").html("");
  var op = 1;
  var jog;
  for(var i = 0;i < 2;i++){
  	if(op == 1){
		jog = 'X';
	  }else{
		jog = 'O';
	  }
    if(jogo[0]== op && jogo[1] == op && jogo[2] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[3]== op && jogo[4] == op && jogo[5] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[6]== op && jogo[7] == op && jogo[8] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[0]== op && jogo[3] == op && jogo[6] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[1]== op && jogo[4] == op && jogo[7] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[2]== op && jogo[5] == op && jogo[8] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[0]== op && jogo[4] == op && jogo[8] == op){
    	$("span").html("'"+jog+"' Venceu!!");
    }else if(jogo[2]== op && jogo[4] == op && jogo[6] == op){
      $("span").html("'"+jog+"' Venceu!!");
    }
    op = 2;
  }
}

$(function(){

	setInterval(function () {
		for (var a=0;a < $(".casa").length;a++){
			jogo[a] = 0;
		}
		var tam = $(".casa").length;
		var tamX = $(".X").length;
		var tamO = $(".O").length;
		for (var a=0;a< tam;a++){
			var pos = $(".casa").eq(a).offset();
			for (var b=0;b<tamX;b++){
				var posX = $(".X").eq(b).offset();
				if((posX.left + 70) > pos.left && (posX.top + 70) > pos.top && (posX.left + 70) < pos.left + 140 && (posX.top + 70) < pos.top + 140){
					jogo[a] = 1;
					console.log("X "+a);
				}
			}
			for (var c=0;c<tamO;c++){
				var posO = $(".O").eq(c).offset();
				if((posO.left + 70) > pos.left && (posO.top + 70) > pos.top && (posO.left + 70) < pos.left + 140 && (posO.top + 70) < pos.top + 140){
					jogo[a] = 2;
					console.log("0 "+a);
				}
			}
		}
		console.log("teste");
		teste();
	},500)



	$(".X").bind("click",function () {
		if(clicou == 0){
			clicou = 1;
			$(this).bind("mousemove",function (e) {
				var x = e.originalEvent.pageX;
				var y = e.originalEvent.pageY;
				$(this).css("left",x-70);
				$(this).css("top",y-70);
			})
		}else{
			clicou = 0;
			$(this).unbind("mousemove")
		}
	})

	$(".O").bind("click",function () {
		if(clicou == 0){
			clicou = 1;
			$(this).bind("mousemove",function (e) {
				var x = e.originalEvent.pageX;
				var y = e.originalEvent.pageY;
				$(this).css("left",x-70);
				$(this).css("top",y-70);
			})
		}else{
			clicou = 0;
			$(this).unbind("mousemove")
		}
	})

})