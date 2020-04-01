<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>1</title>
</head>
<body>
<% if(request.getParameter("name") == null){ %>
	<jsp:forward page="el.html"></jsp:forward>
<% } %>

표현식 사용 : <%=request.getParameter("name") %>

<br>
스크립트릿 사용 : 
<%
	out.println(request.getParameter("name"));
%>

<br>
EL 사용 : ${param.name } el은 표현만 가능, 제어문 없음, 그래서 jstl을 사용, jstl은 외부에서 참조(제이쿼리같이)
</body>
</html>