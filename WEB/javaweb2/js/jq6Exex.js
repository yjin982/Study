function func(arg) {
	var text = $.trim(arg);
	$("#disp_2").empty();			
	// jQuery에 ajax 쓰기
	$.ajax({
		type : "get",
		url : "jq6ExbuserXML2.jsp?jikwon_name="+text,
		dataType : "xml",
		success : function(data) {			
			var str = "";
			str +="<table border = '1'>"
			str +="<tr><th>고객명</th><th>고객전화</th><th>성별</th></tr>"
			$(data).find("jikwon").each(function(){
				str += "<tr>";
				str += "<td>" + $(this).find("gogek_name").text() + "</td>";							
				str += "<td>" + $(this).find("gogek_tel").text() + "</td>";
				str += "<td>" + $(this).find("gogek_jumin").text() + "</td>";
				str += "</tr>";
			});
			str +="</table>"
			$("#disp_2").append(text+"  직원의 고객명단")
			$("#disp_2").append(str)		
		},
		error : function() {
		}
	});
}


$(document).ready(function() {

$("#btnGO").on("click", function() {
		$("#disp").empty();	
		var text = $("#input").val();
		
		// jQuery에 ajax 쓰기
		$.ajax({
			type : "get",
			url : "jq6ExbuserXML.jsp?buser_name=" + text,
			dataType : "xml",
			success : function(data) {
				var str = "";
				var count = 0;
				str +="<table border = '1'>"
				str +="<tr><th>사번</th><th>직원명</th><th>부서전화</th><th>관리고객 </th></tr>"
				$(data).find("jikwon").each(function() {
					count++;
					
					str += "<tr>";
					str += "<td>" + $(this).find("jikwon_no").text() + "</td>";
					
					if($(this).find("gogek_manage").text() > 0){
						str += "<td><a href=\"javascript:func('" + $(this).find("jikwon_name").text() + "')\">" + $(this).find("jikwon_name").text() + "</a>" + "<br></td>";
					}else{
						str += "<td>" + $(this).find("jikwon_name").text() + "</td>";
					}
					
					str += "<td>" + $(this).find("buser_tel").text() + "</td>";
					str += "<td>" + $(this).find("gogek_manage").text() + "</td>";
					str += "</tr>"
					
				});
				str +="</table>"
				$("#disp").append(str)
				$("#disp").append("직원수:"+count)
				
			},
			error : function() {
			}
		
		});
	});
	
});