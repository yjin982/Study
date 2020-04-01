<%@page import="pack.SangpumDto"%>
<%@page import="java.util.ArrayList"%>
<%@page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<jsp:useBean id="connBean" class="pack.ConnBean"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>4</title>
</head>
<body>
<h2>* 상품자료(jsp:Beans O) *</h2>
<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>code</th><th>sang</th><th>su</th><th>dan</th>
	</tr>
	<%
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
</table> <br>
<p/>
<h2>* 상품자료(jstl) *</h2>
<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>code</th><th>sang</th><th>su</th><th>dan</th>
	</tr>
	<% ArrayList<SangpumDto> list2 = connBean.getDataAll(); %>
	<c:forEach var="a" items="<%=list2 %>">
		<tr>
			<td>${a.code}</td>
			<td>${a.sang}</td>
			<td>${a.su}</td>
			<td>${a.dan}</td>
		</tr>
	</c:forEach>
</table>
</body>
</html>