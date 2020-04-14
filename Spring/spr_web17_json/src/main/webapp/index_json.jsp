<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>json - 02</title>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script type="text/javascript">
$(document).ready(function(){
	$("#btnOk").click(() => {
		$("#showdata").html("");
		$.ajax({
			type:"get",
			url:"list",
			data:{"name":"alice"},
			datatype:"json",
			success:(data) => {
				// alert(data); //object로 넘어온거 확인
				// console.log(data);
				let str = "";
				str += data.name + "<br/>";
				str += data.skills[0] + " " + data.skills[1] + "<p/>";
				$("#showdata").html(str);
				
			},error:() => {
				$("#showdata").text("에러 발생!");
			}
		});
	});
	
	$("#btnOk2").click(() => {
		$("#showdata").html("");
		$.ajax({
			type:"get",
			url:"list2",
			dataType:"json",
			success:(data) => {
				//console.log(data);
				let list = data.datas;
				
				let str = "<table>";
				$(list).each((index, obj) => {
					str += "<tr>";
					str += "<td>" + obj["name"] + "</td>";
					str += "<td>" + obj.age + "</td>";
					str += "</tr>";
				});
				str += "</table>";
				
				$("#showdata").html(str);
				
			},error:() => {
				$("#showdata").text("에러2 발생!");
			}
		});
	});
});
</script>
</head>
<body>
Json 자료 읽기 - Ajax<p/>
<input type="button" value="한 개의 자료 읽기" id="btnOk"> <p/>
<input type="button" value="여러 개의 자료 읽기" id="btnOk2"> <p/><br>
<div id="showdata"></div><p/>
</body>
</html>