<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>aop login - 02</title>
</head>
<body>
<% 
	if(session.getAttribute("name") != null){
		out.print("<a href='logout'>로그아웃</a>");
	}
%>
<p/>
<h3>직원 자료</h3>
<table border="1" style="border-collapse: collapse;">
	<tr><th>사번</th><th>이름</th><th>직급</th><th>성별</th><th>부서명</th></tr>
	<c:forEach var="i" items="${list}">
	<tr>
		<td>${i.jikwon_no}</td>
		<td>${i.jikwon_name}</td>
		<td>${i.jikwon_jik}</td>
		<td>${i.jikwon_gen}</td>
		<td>${i.buser_name}</td>
	</tr>
	</c:forEach>
</table>
</body>
</html>