<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="fbean" class="pack.SangpumBean"></jsp:useBean>
<jsp:setProperty property="*" name="fbean"/>

<jsp:useBean id="connBeanPooling" class="pack.ConnBeanPooling"></jsp:useBean>
<% 
	boolean b = connBeanPooling.insertData(fbean); 
	if(b)
		response.sendRedirect("j12db_dbcp.jsp");
	else
		response.sendRedirect("j12db_fail.html");
%>