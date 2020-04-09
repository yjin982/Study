<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
<h2>상품 자료(@MVC + mybatis)</h2>
<table border="1" style="border-collapse: collapse;">
	<tr><th>code</th><th>sang</th><th>su</th><th>dan</th></tr>
	<c:forEach var="i" items="${datas}">
	<tr>
		<td>${i.code}</td>
		<td>${i.sang}</td>
		<td>${i.su}</td>
		<td>${i.dan}</td>
	</tr>
	</c:forEach>
	
	<tr>
		<td colspan="4">
			<form action="search" method="post">
				상품명 검색 
				<input type="text" name="searchValue"> 
				<input type="submit" value="검색">
			</form>
		</td>
	</tr>
</table>
</body>
</html>