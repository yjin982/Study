<%@page import="pack.business.DataDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" 
    pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<jsp:useBean id="processDao" class="pack.business.ProcessDao" />

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
*** 상품 보기(MyBatis) *** <p/>
 <a href="ins.html">상품 추가</a><br>
 <% ArrayList<DataDto> list = (ArrayList)processDao.selectSangDataAll(); %>
 <table border="1" style="border-collapse: collapse;">
 	<tr>
 		<td>code</td><td>sang</td><td>su</td><td>dan</td>
 	</tr>
 	<c:forEach var="s" items="<%=list %>">
 	<tr>
 		<td>${s.code}</td><td>${s.sang}</td><td>${s.su}</td><td>${s.dan}</td>
 	</tr> 	
 	</c:forEach>
 </table>
</body>
</html>