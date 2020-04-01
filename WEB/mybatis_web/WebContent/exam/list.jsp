<%@page import="exam.business.JikwonFormbean"%>
<%@page import="exam.business.JikwonPayDto"%>
<%@page import="exam.business.JikwonDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<jsp:useBean id="processDao" class="exam.business.ProcessDao" />
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>연습문제1</title>
</head>
<body>
직원 자료 출력<br>
<%
	ArrayList<JikwonDto> list = (ArrayList) processDao.selectJikwonAll(); 
	ArrayList<JikwonPayDto> list2 = (ArrayList) processDao.selectJikwonPay(); 
%>
<c:set var="count" value="0" />
<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>사번</th><th>이름</th><th>직급</th><th>성별</th><th>급여</th>
	</tr>
	<c:forEach var="i" items="<%=list %>">
	<tr>
		<td>${i.jikwon_no}</td>
		<td>${i.jikwon_name}</td>
		<td>${i.jikwon_jik}</td>
		<td>${i.jikwon_gen}</td>
		<td>${i.jikwon_pay}</td>
	</tr>
	<c:set var="count" value="${count+1}" />
	</c:forEach>
</table>
인원수 : ${count }명 <br>
<p/>

<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>직급</th><th>인원수</th><th>급여합</th><th>급여평균</th>
	</tr>
	<c:forEach var="i" items="<%=list2 %>">
	<tr>
		<td>${i.jikwon_jik}</td>
		<td>${i.jsu}</td>
		<td><fmt:formatNumber value="${i.jsum}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${i.javg}" pattern="#,##0" /></td>
	</tr>
	</c:forEach>
</table>










<br><br><br><br><br><br>
------------------------------------------------------------------------------------<br>
<c:set var="dto1" value="${processDao.selectJikwonSu('사원')}" />
<c:set var="dto2" value="${processDao.selectJikwonSu('대리')}" />
<c:set var="dto3" value="${processDao.selectJikwonSu('과장')}" />
<c:set var="dto4" value="${processDao.selectJikwonSu('부장')}" />
<c:set var="dto5" value="${processDao.selectJikwonSu('이사')}" />
<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>직급</th><th>인원수</th><th>급여합</th><th>급여평균</th>
	</tr>
	<tr>
		<td>사원</td>
		<td><fmt:formatNumber value="${dto1.jsu}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto1.jsum}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto1.javg}" pattern="#,##0" /></td>
	</tr>
	<tr>
		<td>대리</td>
		<td><fmt:formatNumber value="${dto2.jsu}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto2.jsum}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto2.javg}" pattern="#,##0" /></td>
	</tr>
	<tr>
		<td>과장</td>
		<td><fmt:formatNumber value="${dto3.jsu}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto3.jsum}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto3.javg}" pattern="#,##0" /></td>
	</tr>
	<tr>
		<td>부장</td>
		<td><fmt:formatNumber value="${dto4.jsu}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto4.jsum}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto4.javg}" pattern="#,##0" /></td>
	</tr>
	<tr>
		<td>이사</td>
		<td><fmt:formatNumber value="${dto5.jsu}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto5.jsum}" pattern="#,##0" /></td>
		<td><fmt:formatNumber value="${dto5.javg}" pattern="#,##0" /></td>
	</tr>
</table>
</body>
</html>