<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
String adminId = (String)session.getAttribute("adminKey");

if(adminId == null) {
	response.sendRedirect("adminlogin.jsp");
	return;
}
%>

<table style="width: 80%;">
	<tr style="background-color: #aabbcc; text-align: center;">
		<td><a href="../index.jsp">홈페이지</a></td>
		<td><a href="adminlogout.jsp">로그아웃</a></td>
		<td><a href="membermanager.jsp">회원관리</a></td> <!-- 생략 -->
		<td><a href="productmanager.jsp">상품관리</a></td>
		<td><a href="ordermanager.jsp">주문관리</a></td>
	</tr>
</table>