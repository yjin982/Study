<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% String code = request.getParameter("code"); %>
<jsp:useBean id="connBeanPooling" class="pack.ConnBeanPooling"></jsp:useBean>
<% 
	if(connBeanPooling.deleteData(code))
		response.sendRedirect("j12db_dbcp.jsp");
	else
		response.sendRedirect("j12db_fail.html");
%>