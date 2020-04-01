<%@page import="java.util.Date"%>
<%@page import="java.util.HashMap"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %> <!-- prefix 접두어는 자기 마음대로, 한글도 가능하지만 보통 c(core) 를 많이 씀 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3</title>
</head>
<body>
<b>* JSTL(JSP Standard Tag Library) *</b><hr>
<!-- https://search.maven.org/#browse%7C-658715035 혹은 jar파일 다운로드 받아서 web-inf/lib에 넣은 후 페이지 지시어처럼 선언하기-->
<b>* 변수 연습 * </b><br>
<c:set var="irum" value="홍길동" scope="page"></c:set> <= 변수선언 set scope에 쓸 수 있는 것(page, request, session, application)<br>
<c:out value="${irum}"></c:out> <= 변수 출력 <br>
<c:set var="ir" scope="session">
	한국인
</c:set>
<c:out value="${ir}"></c:out><br>
<c:set var="aa" value="${header['User-Agent']}" scope="page"></c:set> <= aa변수에 header['User-Agent']<br>
aa변수 값은 <c:out value="${aa}"></c:out><br>
<c:remove var="aa"/> <=변수값 지우기(scope 따로 주면 다른 변수가 되므로 안 지워짐)<br>
aa변수 값은 <c:out value="${aa}"></c:out><br>
------------------------<br>
<c:set var="su1" value="10"/>
<c:set var="su2">10.5</c:set>
합은 ${su1+su2} <br>
<p/>
<b>* 조건문(if) *</b><br>
<c:set var="bb" value="star"></c:set>
<c:if test="${bb eq 'star'}"> <!-- eq는 ==와 같음 -->
	if 연습 : bb값은 <c:out value="${bb}"/>
</c:if>
<c:if test="${bb eq 'tar'}"> <!-- 거짓이라 출력 X -->
	if 연습 : bb값은 <c:out value="${bb}"/>
</c:if>
<br>
<c:if test="${bb != null}">
	if 연습2 : 조건 참 bb는 null이 아니므로 출력
</c:if>
<p>
<b>* 조건문(choose) *</b><br>
<c:choose>
	<c:when test="${bb == 'moon'}">
		달이야
	</c:when>
	<c:when test="${bb eq 'star'}">
		 별
	</c:when>
	<c:otherwise>어떠한 조건도 만족하지 않을 경우</c:otherwise>
</c:choose>
<p/>
<b>* 반복문 *</b><br>
<c:forEach var="i" begin="1" end="9">
	<c:out value="${i}"/>&nbsp;&nbsp;
</c:forEach><br>
 - 구구단(3단)<br>
<c:forEach var="su" begin="1" end="9">
	3 * ${su} = ${3*su} &nbsp;&nbsp;
</c:forEach><br>
 - header 정보 출력(컬렉션 출력)<br>
<c:forEach var="h" items="${headerValues}">
	속성 : <c:out value="${h.key}" />&nbsp;&nbsp;
	값 : <c:forEach var="k" items="${h.value }">
			${k}<br>
		</c:forEach>
</c:forEach>
<%
	HashMap map = new HashMap();
	map.put("name", "신기해");
	map.put("today", new Date());
%>
 - 내가 만든 변수(hashmap) 출력<br>
<c:set var="m" value="<%=map%>" />
<c:forEach var="i" items="${m}">
	${i.key} : ${i.value} &nbsp;&nbsp;&nbsp; 
</c:forEach><br>
<c:set var="arr" value="<%=new int[]{1,2,3,4,5,6,7,8,9,10,11,12} %>" />
<c:forEach var="i" items="${arr}" begin="2" end="11" step="2">
	${i} &nbsp;&nbsp;
</c:forEach><br>
 - 문자열 분할 (forTokens)<br>
<c:forTokens var="animal" items="horse,tiger,lion,pig,cat,dog" delims="," varStatus="num">
	동물${num.count} : ${animal} &nbsp;&nbsp;
</c:forTokens>
<p/>
<b>* 숫자 및 날짜 관련 서식 *</b><br>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<hr>
숫자 : <fmt:formatNumber value="12345.6789" type="number" /><br>
통화 :  <fmt:formatNumber value="12345.6789" type="currency" currencySymbol="$" /><br>
백분율 :  <fmt:formatNumber value="12345.6789" type="percent"  /><br>
소수이하 :  <fmt:formatNumber value="12345.6789" type="number" pattern="#,##0.0" /><br>
소수이하 :  <fmt:formatNumber value="12345.6789" type="number" pattern="0,000.0" /><br>
자리채우기 :  <fmt:formatNumber value="1.6789" type="number" pattern="#,##0.0" /><br>
자리채우기 :  <fmt:formatNumber value="1.6789" type="number" pattern="0,000.0" /><br>
<br>
<c:set var="now" value="<%=new Date() %>" />
<c:out value="${now}" /><br>
<fmt:formatDate value="${now}" type="date"/><br>
<fmt:formatDate value="${now}" type="time"/><br>
<fmt:formatDate value="${now}" type="both"/><br>
<fmt:formatDate value="${now}" type="both" pattern="yyyy년 MM월 dd일"/><br>
</body>
</html>