<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String irum = request.getParameter("name");
String id = request.getParameter("id");
String nai = request.getParameter("age");

if(!id.equals("aaa"))
	response.sendRedirect("js11.html");



%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
전달 받은 자료는 <br>
이름은 <%=irum %>이고 나이는 <%=nai %>
</body>
</html>