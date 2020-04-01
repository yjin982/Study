<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr"></jsp:useBean>

<%
	String spage = request.getParameter("page");
	String num = request.getParameter("num");
	String pass = request.getParameter("pass");
	boolean b = boardMgr.chkPass(Integer.parseInt(num), pass); //비번 확인
	
	if(b){ //true = 비밀번호 맞음
		boardMgr.delData(num);
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