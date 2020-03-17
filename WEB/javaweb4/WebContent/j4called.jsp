<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
서블릿에 의해 호출된 jsp 파일 <br>
<%
	request.setCharacterEncoding("utf-8");

	//리다이렉트 방식일 때
	String data = request.getParameter("data");
	out.println("리다이렉트 자료는 " + data);
	/////주소 http://localhost/javaweb4/j4called.jsp?data=tom
%>
<br>
<%
	//포워드 방식일 때
	String data2 = (String)request.getAttribute("key"); //객체로 넘겨주기때문에 캐스팅이 필요
	out.println("포워드 자료는 " + data2);
	/////주소 : http://localhost/javaweb4/irum.go
%>
</body>
</html>