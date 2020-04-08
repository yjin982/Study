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
<h2>회원 자료 보기 - (@MVC - jdbcDaoSupport 스프링 제공)</h2>

<c:if test="${count == 0}">
	출력 자료가 없습니다.<p/>
	<a href="insert">추가</a>
</c:if>
<c:if test="${count > 0}">
	<table border="1" style="border-collapse: collapse; width: 200px;">
		<tr>
			<th colspan="2"><a href="insert">추가</a></th>
		</tr>
		<tr>
			<th>id</th><th>name</th>
		</tr>
		<c:forEach var="i" items="${list}">
		<tr>
			<td>${i.id}</td>
			<td><a href="detail?id=${i.id}">${i.name}</a></td>
		</tr>
		</c:forEach>
		<tr>
			<td colspan="2" style="text-align: center;">
				<c:set var="pageCount" value="${(count - 1) / pageSize + 1}" />
				<c:forEach var="p" begin="1" end="${pageCount}">
					<c:if test="${currentPage == p}">${p}</c:if>
					<c:if test="${currentPage != p}"><a href="list?pageNum=${p}">${p}</a></c:if>
				</c:forEach>
			</td>
		</tr>
	</table>
	
</c:if>


<br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><hr>
페이징처리 안한 것<br>
<table border="1" style="border-collapse: collapse; width: 200px;">
	<tr>
		<th colspan="2"><a href="insert">추가</a></th>
	</tr>
	<tr>
		<th>id</th><th>name</th>
	</tr>
	<c:forEach var="i" items="${list}">
	<tr>
		<td>${i.id}</td>
		<td><a href="detail?id=${i.id}">${i.name}</a></td>
	</tr>
	</c:forEach>
</table>
</body>
</html>