<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>

 <jsp:useBean id="bean" class="pack.business.DataBean" />
 <jsp:setProperty property="*" name="bean"/>
 <jsp:useBean id="processDao" class="pack.business.ProcessDao" />
 
 <%
 	processDao.insData(bean);
 	response.sendRedirect("list.jsp");
 %>