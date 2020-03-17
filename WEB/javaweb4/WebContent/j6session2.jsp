<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>선택 결과 보기</h2>
<%
	request.setCharacterEncoding("utf-8");
	
	String movie = request.getParameter("movie");
	String id = (String)session.getAttribute("idkey");
	
	if(id != null){
%>
		<%=id%> 님이 좋아하는 영화는 <%=movie %>입니다.<br>
		세션 아이디 : <%=session.getId() %><br>
		세션 유효시간 : <%=session.getMaxInactiveInterval() %><br>		
<%}else{%>
	세션이 설정되지 않음<br>
<%}%>
</body>
</html>