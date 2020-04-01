<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.business.DataFormBean" />
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="memberProcess" class="pack.business.MemberProcess" />

<%
	boolean b = memberProcess.updateData(bean);

	if(b){
		response.sendRedirect("list.jsp");
	}else{
		response.sendRedirect("fail.jsp");
	}

%>
