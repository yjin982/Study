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
		speech.animate({fontSize:num + 'px'}, 'fast'); // fast, slow ,1000, 2000 ...
	});
	
	//문서의 일부 보이기 and 숨기기
	 var firstPara = $("p:eq(2)"); // p태그 중  첫번째를 선택
	 firstPara.hide();
	 $("a.more").click(function(){ // a 태그 중 id가 more인 태그를 클릭하면
		 // alert(firstPara.is(":hidden")); // firstPara가 hidden상태인지를 확인 (true)
		 if(firstPara.is(":hidden")) {
			 //firstPara.fadeIn("slow"); //효과를 줘서 보이게 함.(fadein, fadeout 효과)
			 firstPara.slideToggle("slow"); 
			 $(this).text("read less"); //현재 이벤트가 발생한 태그의 텍스트를 변경
		 }else{
			 firstPara.slideToggle("slow"); //slide 효과
			 $(this).text("read more");
		 }
	 });
	 
	 
	 $("button, a.more").hover(
			 function(){
				 $(this).addClass("myHover");
			 },
			 function(){
				 $(this).removeClass("myHover");
			 }
	 );
	
});