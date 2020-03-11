<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% 
request.setCharacterEncoding("utf-8");
String irum = request.getParameter("name");
String nai = request.getParameter("age");


%>
<%=irum + "님의 나이는 " + nai%>