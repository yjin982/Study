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
<h3>미니 게시판</h3>
<a href="insert">글쓰기</a><p/>
<table border="1" cellpadding="5" style="border-collapse: collapse; width: 800px; ">
	<tr>
		<th width="50">번호</th><th width="500">제목</th><th width="200">작성자</th><th width="50">조회수</th>
	</tr>
	<c:forEach var="i" items="${list}">
	<tr>
		<td align="center">${i.num}</td>
		<td>
			<a href="detail?num=${i.num}">${i.title}</a>
		</td>
		<td>${i.author}</td>
		<td align="center">${i.readcnt}</td>
	</tr>
	</c:forEach>
	<tr>
		<td colspan="4" style="text-align: center;">
			<form action="search" method="post">
				<select name="searchName">
					<option value="author" selected="selected">작성자</option>
					<option value="title">글 제목</option>
				</select>
				<input type="text" name="searchValue"> 
				<input type="submit" value="검색">
			</form>
		</td>
	</tr>
</table>
</body>
</html>