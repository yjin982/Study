<%@page import="javax.websocket.SendResult"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="memberBean" class="pack.member.MemberBean"></jsp:useBean>
<jsp:setProperty property="*" name="memberBean"/>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr"></jsp:useBean>
<%
	boolean b = memberMgr.loginCheck(memberBean.getId(), memberBean.getPasswd());

	if(b){
		session.setAttribute("idKey", memberBean.getId());
		response.sendRedirect("../index.jsp");
	}else{
		response.sendRedirect("loginfail.html");
	}
%>