<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ajax&mybatis - 02</title>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
	$(".showdata").empty();
	
	$.ajax({
		type:"get",
		url:"sangpum",
		dataType:"json",
		success:(sangpumData) => {
			//console.log(sangpumData);
			let list = sangpumData.sangpums;
			
			let str = "<table>";
			str += "<tr><th>code</th><th>sang</th><th>su</th><th>dan</th></tr>"
			$(list).each((index, obj) => {
				str += "<tr>";
				str += "<td>" + obj["code"] + "</td>";
				str += "<td>" + obj.sang + "</td>";
				str += "<td>" + obj.su + "</td>";
				str += "<td>" + obj.dan + "</td>";
				str += "</tr>";
			});
			str += "</table>";
			
			$(".showdata").append(str);
		},
		error: () => {
			$(".showdata").text("error!");
		}
	});
});
</script>
</head>
<body>
<h3>상품정보 (@MVC-mybatis-Ajax)</h3>
<div class="showdata"></div>
</body>
</html>