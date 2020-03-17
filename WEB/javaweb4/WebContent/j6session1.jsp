<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id");
	
	session.setAttribute("idkey", id);
	session.setMaxInactiveInterval(10); //세션 유효시간 10초
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>세션 연습 중</h2>
<form action="j6session2.jsp" method="post">
	* 좋아하는 영화는? * <br>
	<input type="radio" name="movie" value="기생충" checked="checked">기생충&nbsp;&nbsp;
	<input type="radio" name="movie" value="작은아씨들">작은 아씨들&nbsp;&nbsp;
	<input type="radio" name="movie" value="정직한후보">정직한 후보&nbsp;&nbsp; <p/>
	<input type="submit" value="결과 보기">
</form>
</body>
</html>