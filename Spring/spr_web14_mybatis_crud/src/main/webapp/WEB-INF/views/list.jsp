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
<h3>회원 정보(@MVC - mybatis CRUD)</h3>
<a href="insert">회원 추가</a><p/>

<table border="1" style="border-collapse: collapse;">
	<tr><th>번호</th><th>이름</th><th>주소</th><th>변경</th></tr>
	<c:forEach var="i" items="${list}">
	<tr>
		<td>${i.num}</td>
		<td>${i.name}</td>
		<td>${i.addr}</td>
		<td>
			<a href="update?num=${i.num}">수정</a> / 
			<a href="delete?num=${i.num}">삭제</a>
		</td>
	</tr>
	</c:forEach>
</table>
</body>
</html>