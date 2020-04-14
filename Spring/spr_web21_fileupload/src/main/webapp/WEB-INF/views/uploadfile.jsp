<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>파일 업로드 - 03</title>
</head>
<body>
<h3>업로드된 파일 정보</h3>
파일명 : ${filename} <hr>
<form action="download" method="post">
	<input type="hidden" name="filename" value="${filename}">
	<input type="submit" value="현재 파일 다운로드 하기">
</form>
</body>
</html>