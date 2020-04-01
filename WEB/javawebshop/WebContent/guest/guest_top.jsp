<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<%
	String memid = (String)session.getAttribute("idKey");

	String log = "";
	if(memid == null)
		log = "<a href='../member/login.jsp'>로그인</a>";
	else
		log = "<a href='../member/logout.jsp'>로그아웃</a>";
	
		
	String mem = "";	
	if(memid == null)
		mem = "<a href='../member/register.jsp'>회원가입</a>";
	else
		mem = "<a href='../member/memberupdate.jsp'>회원정보 수정</a>";
%>


<div style="width:80%; margin-left:10%;">
<table class="table table-borderless" ">
	<tr>
		<th><%=log %></th>
		<th><%=mem %></th>
		<th><a href="productlist.jsp">상품목록</a></th>
		<th><a href="cartlist.jsp">장바구니</a></th>
		<th><a href="orderlist.jsp">구매목록</a></th>
		<th><a href="../board/boardlist.jsp">게시판</a></th>
	</tr>
</table>
</div>