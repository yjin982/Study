<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	//현재 jsp 파일은 BL(Business Logic)을 담당, 출력용 X
	request.setCharacterEncoding("utf-8");
	String data = request.getParameter("data");
	String msg = "Mr." + data;
	
	
	//1. 리다이렉트
	//response.sendRedirect("j5called.jsp?data=" + msg);
	
	
	//2. 포워드
	request.setAttribute("data", msg);
	
	ArrayList<String> list = new ArrayList<String>(); //db에서 읽었다고 가정
	list.add("tom");
	list.add("oscar");
	list.add("alex");
	request.setAttribute("friend", list); //객체 넘겨주기 확인
	
	//RequestDispatcher dispatcher = request.getRequestDispatcher("j5called.jsp");
	//dispatcher.forward(request, response);
%>
<jsp:forward page="j5called.jsp"></jsp:forward> <!-- jsp이기 때문에 액션태그로 활용해도 같은 결과 -->
<!-- *추가* 
WEB-INF 아래에 부를 파일을 만들고 부를려고 할 때 포워딩만 가능
여기는 보안상 
-->