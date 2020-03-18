<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="fbean" class="pack.SangpumBean"></jsp:useBean>
<jsp:setProperty property="*" name="fbean"/>

<jsp:useBean id="connBeanPooling" class="pack.ConnBeanPooling"></jsp:useBean>
<% 
	boolean b = connBeanPooling.updateData(fbean);
	//실제로는 '정말로 수정하시겠습니까' 같은 안내메세지를 띄우는게 좋음
	if(b)
		response.sendRedirect("j12db_dbcp.jsp");
	else
		response.sendRedirect("j12db_fail.html");
%>