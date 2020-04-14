<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>ex - 02</title>
<script src="http://code.jquery.com/jquery-latest.min.js"></script>
<script type="text/javascript">
function ci(no){
	$(".jikwonlist").empty();
	$.ajax({
		type:"get",
		url:"buserjikwon?buser_no=" + no,
		dataType:"json",
		success:(data) => {
			let list = data.j;
			let count = 0;
			
			let str = "<table border='1' style='border-collapse: collapse;'>";
			str += "<tr><th>사번</th><th>이름</th><th>직급</th><th>고객 유무</th></tr>"
			$(list).each((index, obj) => {
				str += "<tr>";
				str += "<td>" + obj.jikwon_no + "</td>";
				str += "<td>" + obj.jikwon_name + "</td>";
				str += "<td>" + obj.jikwon_jik + "</td>";
				str += "<td>" + obj.jikwon_go + "</td>";
				str += "</tr>";
				count++;
			});
			str += "</table>";
			str += "<p/>인원수 : " + count + "명";
				
			$(".jikwonlist").append(str); 
		},
		error:() => {
			$(".jikwonlist").text("error!!!");
		}
	});
}
</script>
</head>
<body>
<% String id = (String) session.getAttribute("id"); %>
<h3><%=id %>님 반갑습니다.&nbsp;&nbsp;&nbsp;&nbsp;<a href="logout">로그아웃</a></h3>
<hr>

<h3>부서 목록</h3>
<table border='1' style='border-collapse: collapse;'>
	<tr><th>부서번호</th><th>부서명</th><th>부서 전화</th></tr>
	<c:forEach var="i" items="${list}">
		<tr>
			<td>${i.buser_no}</td>
			<td><a href="#" onClick="ci(${i.buser_no});">${i.buser_name}</a></td>
			<!-- 또는 <a href="javascript:ci(${i.buser_no});">${i.buser_name}</a> -->
			<td>${i.buser_tel}</td>
		</tr>
	</c:forEach>
</table><p/>
<br>
<h3>근무자 정보</h3>
<div class="jikwonlist"></div><p/>
</body>
</html>