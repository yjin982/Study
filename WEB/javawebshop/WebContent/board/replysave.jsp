<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.board.BoardBean"></jsp:useBean>
<jsp:setProperty property="*" name="bean"/>
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr"></jsp:useBean>
 <%
 	String spage = request.getParameter("page");
 	int num = bean.getNum();
 	int gnum = bean.getGnum();
 	int onum = bean.getOnum() + 1;
 	int nested = bean.getNested() + 1;
 	
 	//onum 갱신  - 원글의 첫번째 댓글이면 +1, 원글의 두번째 댓글이면 현재 댓글은 1, 이전 댓글은 +1
 	//같은 그룹 내에서 새로운 댓글의 onum보다 크거나 같은 값을 댓글 입력 전에 먼저 수정하기, 작으면 수정 X
 	boardMgr.updateOnum(gnum, onum); //onum갱신
 	
 	//댓글 저장 준비
 	bean.setOnum(onum);
 	bean.setNested(nested);
 	bean.setBip(request.getRemoteAddr());
 	bean.setNum(boardMgr.currentGetNum()+1);
 	bean.setBdate();
 	
 	boardMgr.saveReplyData(bean); //댓글 저장
 	response.sendRedirect("boardlist.jsp?page=" + spage); //댓글 작성 후 목록 보기
 %>