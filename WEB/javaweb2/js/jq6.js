$(document).ready(function(){
	/////xml
	$("#btn1").on("click", function(){
		$("#disp").empty();
		$.ajax({
			type:"get",
			url:"jq6xml1.jsp",
			dataType:"xml",
			success:function(data){
				var str = "";
				$(data).find("person").each(function(){
					str += $(this).find("irum").text() + "&nbsp;";
				}); //화살표 함수에서는 this가 안됨
				$("#disp").append(str);
				
			},error:function(){
				alert("error");
				
			},statusCode:{ //이부분까지는 잘 안함
				200:function(){
					console.log("읽기 성공");
				},
				404:function(){
					console.log("찾기 실패");
				}
			}
		});
	});
	
	/*$("#btn2").on("click", function(){
		$("#disp").empty();
		
	});*/
	$("#btn2").on("click", () => {
		$("#disp").empty();
		//var aa = $.ajax({  //로 변수로 받아서 하는 경우도 있음
		$.ajax({
			type:"post", //xml은 get, post 구분하지 않기 때문에 post로 해도 가능
			url:"jq6xml2.jsp",
			//data:"irum=" + "손오공",
			data:{"irum":"삼장법사"},
			dataType:"xml",
			success:function(data){
				var str = "";
				$(data).find("person").each(function(){
					str += $(this).find("irum").text() + "&nbsp;";
				});
				$("#disp").append(str);
				
			},error:function(){
				alert("error");
			}
		});
	});
	
	
	/////json
	$("#btn3").on("click", () => {
		$("#disp").empty();
		$.ajax({
			type:"get",
			url:"jq6json1.jsp",
			dataType:"json",
			success:(data) => {
				var str = "";
				$.each(data, (index, entry) => { //json은 find X
					str += entry["name"] + ", " + entry.age; //name, age 둘 방법 다 가능
				});
				$("#disp").append(str);
				
			}, error: () => {
				console.log("err");
			}
		});
	});
	
	$("#btn4").on("click", () => {
		$("#disp").empty();
		$.ajax({
			type:"get",
			url:"jq6json2.jsp",
			//data:"irum=" + "장비" + "&nai=" + "34",
			data:{"irum":"유비", "nai":"50"},
			dataType:"json",
			success:(data) => {
				var str = "";
				$.each(data, (index, entry) => { //json은 find X
					str += entry["name"] + ", " + entry.age; //name, age 둘 방법 다 가능
				});
				$("#disp").append(str);
				
			}, error: () => {
				console.log("err");
			}
		});
	});
});