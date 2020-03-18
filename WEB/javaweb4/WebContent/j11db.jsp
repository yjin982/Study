<%@page import="pack.SangpumDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="connBean" class="pack.ConnBean"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>* 상품자료(jsp:Beans O) *</h2>
<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>code</th><th>sang</th><th>su</th><th>dan</th>
	</tr>
	<% //j7db.jsp와 비교 / 현재로써 이 부분 자바는 어쩔수없다 => EL로 해결
		ArrayList<SangpumDto> list = connBean.getDataAll();
		for(SangpumDto s:list){
	%>
	<tr>
		<td><%=s.getCode() %></td>
		<td><%=s.getSang() %></td>
		<td><%=s.getSu() %></td>
		<td><%=s.getDan() %></td>
	</tr>
	<%
		}
	%>
</table>
</body>
</html>