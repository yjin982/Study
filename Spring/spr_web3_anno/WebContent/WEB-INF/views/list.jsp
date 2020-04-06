<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
컨트롤러 처리 후 결과 : <br>
<%
	String ss = (String)request.getAttribute("key");
%>
<%=ss %>
</body>
</html>