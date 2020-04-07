<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
인사말 : 
<% 
//	request.setCharacterEncoding("utf-8");
//	String ss = request.getParameter("result");
//	out.println(ss);
%>
${requestScope.result}
</body>
</html>