<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.board.BoardBean"></jsp:useBean>
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr"></jsp:useBean>

<%
	String spage = request.getParameter("page");
	boolean b = boardMgr.chkPass(bean.getNum(), bean.getPass()); //비번 확인
	
	if(b){ //true = 비밀번호 맞음
		boardMgr.saveEditData(bean);
		response.sendRedirect("boardlist.jsp?page=" + spage);
	}else {
%>
<script type="text/javascript">
	alert("비밀번호 불일치!");
	history.back(); ///// == history.go(-1);    location.href="파일명"
</script>
<%		
	}
%>