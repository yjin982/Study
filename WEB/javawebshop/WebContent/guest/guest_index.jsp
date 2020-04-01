<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>쇼핑몰 메인</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="../js/script.js"></script>
<style type="text/css">
	 h2 a:link { text-decoration: none;}
	 h2 a:visited {text-decoration: none;}
	 h2 a:hover {text-decoration: none;}
</style>
</head>
<body>
<h2 style="margin:30px; text-align: center;"><a href="guest_index.jsp"> 전문 쇼핑몰 </a></h2>
<%@include file="guest_top.jsp" %>
<div style="margin:30px;">
<table style="width: 100%;">
<% if(memid != null){ //top.jsp에서 include했기 때문에%>
	<tr>
		<td style="text-align: center;">
			<%=memid %>님, 방문을 환영합니다!<img src="../images/pic2.gif">
		</td>
	</tr>
<%}else{ %>
	<tr style="text-align: center;">
		<td style="font-size: 20px; background-image: url(../images/pic.jpg); background-size: 100%;">
			<br><br><br><br><br>
			<span style="background-color: white;">고객님 어서오세요!</span>
			<br><br><br><br><br>
			<span style="background-color: white;">로그인 후 사용이 가능합니다.</span>
			<br><br><br><br><br><br><br><br><br><br>
		</td>
	</tr>
<%} %>
</table>
</div>



<%@include file="guest_bottom.jsp" %>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>