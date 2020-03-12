$(document).ready(function(){
	//1. html 읽기
	$("#test1").click(function(){
		$("#disp").empty();
		$("#disp").load("jq5h.html");
	});
	
	//2. json 읽기1
	$("#test2").click(function(){
		$("#disp").empty();

		$.getJSON("jq5j1.json", function(data){
			//alert(data); //오브젝트로 데이터 넘어 오는 것 확인
			
			$.each(data, function(keyindex, value){ //객체를 반복할 때
				//console.log(keyindex + " " + value);
				var str = "<ol>";
				str += "<li>" + value["title"] + "</li>";
				str += "<li>" + value["desc"] + "</li>";
				str += "<li>" + value["author"] + "</li>";
				str += "</ol>";
				
				$("#disp").append(str);
			});
		});
	});
	
	
	//3. json 읽기2
	$("#test3").click(function(){
		$("#disp").empty();
		var items = [];
		
		console.log("1");
		$.getJSON("jq5j2.jsp", function(data){
			
			console.log("2");
			$.each(data, function(keyindex, value){
				console.log("3");
				var str = "<ol>";
				str += "<li>" + value["code"] + "</li>";
				str += "<li>" + value["sang"] + "</li>";
				str += "<li>" + value["su"] + "</li>";
				str += "<li>" + value["dan"] + "</li>";
				str += "</ol>";
				
				//$("#disp").append(str);
				items.push(str);
			});
			
			$("<b/>", {html:items}).appendTo("#disp");
		});
	});
	
	
	//4. xml 읽기1
	$("#test4").click(function(){
		$("#disp").empty();
		
		$.get("jq5x1.xml", function(data){
			//alert(data); //alert($(data).find("aa").size());
			
			$(data).find("aa").each(function(){
				var fdata = $(this); //현재 읽힌 aa 요소
				var str = "<div>";
				str += fdata.attr("part") + " " + fdata.attr("term");
				str += " - ";
				str += fdata.find("desc").text();
				str += "</div>";
				console.log(str);
				$("#disp").append(str);
				
			});
		});
		
	});
	
	
	//5. xml 읽기2
	$("#test5").click(function(){
		$("#disp").empty();
		
		$.post("jq5x2.jsp", function(data){
			$(data).find("sangpum").each(function(){
				var sangpum = $(this);
				
				var str = "<div>";
				str += sangpum.find("code").text() + " ";
				str += sangpum.find("sang").text() + " ";
				str += sangpum.find("su").text() + " ";
				str += sangpum.find("dan").text() + " ";
				str += "</div>";
				
				$("#disp").append(str);
			});
		});
	});
});