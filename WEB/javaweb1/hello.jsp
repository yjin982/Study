<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% 
request.setCharacterEncoding("utf-8");
String ir = request.getParameter("irum");
String nai = request.getParameter("nai");
System.out.println("이름은 " + ir + " 나이는 " + nai);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
jsp 파일
</body>
</html>