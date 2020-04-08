<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>4</title>
</head>
<body>
<h2>상세 보기</h2>
<table border="1" style="border-collapse: collapse; width: 200px;">
	<tr>
		<td>id</td><td>${member.id}</td>
	</tr>
	<tr>
		<td>pw</td><td>${member.passwd}</td>
	</tr>
	<tr>
		<td>name</td><td>${member.name}</td>
	</tr>
	<tr>
		<td>regdate</td><td>${member.regdate}</td>
	</tr>
	<tr>
		<td colspan="2" style="text-align: center;">
			<a href="list">목록</a> 
			<a href="update?id=${member.id}">수정</a> 
			<a href="delete?id=${member.id}">삭제</a>
		</td>
	</tr>
</table>
</body>
</html>