<%@page import="pack.Student"%>
<%@page import="pack.Person"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>5</title>
</head>
<body>
<b>* 서블릿에서 작성한 객체 출력*</b><br/>
전통적 방식(스크립트릿) : 안녕 <%=request.getAttribute("man") %> &nbsp;&nbsp;&nbsp;
EL : 안녕 ${requestScope.man} / ${man} (requestScope는 많이 쓰이니까 생략가능) <br>

전통 : <%Person p = (Person)request.getAttribute("person"); %> <%=p.getName() %>&nbsp;&nbsp;&nbsp;
EL : ${person.name }<br>

전통 : <%Student s = (Student)request.getAttribute("student"); %> <%=s.getAge() %>&nbsp;&nbsp;&nbsp;
EL : ${student.age }<br>

전통 : <%=request.getAttribute("animal") %>&nbsp;&nbsp;&nbsp;
EL : ${animal[0]}, ${animal[1]}, ${animal["2"]}<br>

<br>
<c:if test="${list != null }">
	<c:forEach var="a" items="${list}">
		${a[0]}, ${a[1]}, ${a[2]}<br>
	</c:forEach>
</c:if>

<br><br>
<c:if test="${list != null }">
	<c:forEach var="a" items="${list}">
		<c:forEach var="b" items="${a}">
			${b}
		</c:forEach>
	</c:forEach>
</c:if>
<br>

<c:choose>
	<c:when test="${list eq null}">자료없음</c:when>
	<c:otherwise>자료있음</c:otherwise>
</c:choose><br>
<hr>

<b>* try~except 처리 *</b><br>
<c:catch var="myErr">
	<% 
		int a = 10 / 0; 
		out.println(a);	
	%>
</c:catch>
<c:if test="${myErr != null }"> <!-- null이 아니면 에러 -->
	에러 발생 : ${myErr.message}
</c:if><br>
<br>
<b>다른 문서 포함</b><br>
include 지시어 사용 : <%@include file="poham.jsp" %><br>
jsp action tag 사용 : <jsp:include page="poham.jsp" /> <br>
jstl 사용 : <c:import url="poham.jsp" /> <br>

<br>
<c:import url="https://www.daum.net" /><br>
<br>
<c:set var="url" value="https://www.naver.com" />
<c:import url="${url}" var="u" />
<b><c:out value="${url}"></c:out></b>
<c:out value="${u}"></c:out>
</body>
</html>