$(document).ready(function(){
	var speech = $("div.speech");
	
	var defaultFsize = speech.css("fontSize"); // 폰트 사이즈 가져오기
	
	$("#switchter button").click(function(){ //switchter 자식들 button
		var num = parseInt(speech.css("fontSize")); // 그냥 가져오면 뒤에 px가 붙기 때문에 parse
		
		switch(this.id){
		case "switcher-default":
			num = parseFloat(defaultFsize, 10);
			break;
		case "switcher-large":
			num += 8;
			break;
		case "switcher-small":
			num -= 8;
			break;
		}
		
		//speech.css("fontSize", num); //이렇게 주면 끊어짐
		speech.animate({fontSize:num + 'px'}, 'fast');
	});
});