<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>jsp가 넘겨준 자료</h2>
<%
	//현재 jsp 파일은 view 담당
	
	//1. 리다이렉트
	//String data = request.getParameter("data");
	//out.println("data : " + data);
	//주소 :  j5call.jsp에서 => http://localhost/javaweb4/j5called.jsp?data=Mr.james
%>
<br>
<%
	//2. 포워드
	String data = (String)request.getAttribute("data");
	out.println("data : " + data);
%>
<br>
<%
	ArrayList<String> mylist = (ArrayList<String>)request.getAttribute("friend");
	out.println("친구들 : ");
	for(String my:mylist){
		out.print(my + " ");
	}
	
	//주소 : http://localhost/javaweb4/j5call.jsp
%>
</body>
</html>