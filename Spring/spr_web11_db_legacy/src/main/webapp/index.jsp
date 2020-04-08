<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>1</title>
</head>
<body>
<!-- <a href="testdb">Go</a> -->
링크를 안 걸려면 response.sendRedirect
<% response.sendRedirect("testdb"); %>
</body>
</html>