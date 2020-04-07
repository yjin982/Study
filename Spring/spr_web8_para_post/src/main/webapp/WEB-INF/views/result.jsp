<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="c"  uri="http://java.sun.com/jsp/jstl/core"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
폼빈 사용<p/>
결과 = [${data}]
<hr>
참고 : 객체로 만들었기 때문에 가능<br>
${sangpumBean.sang} <= 달러{sangpumBean.sang}(@ModelAttribute("my") 걸기 전) <p/>
${my.sang } <= 달러{my.sang}(@ModelAttribute("my") 건 후, 별명으로 접근) <p/>
[<%
	ArrayList<String> list = (ArrayList)request.getAttribute("myList");
	for(String i : list){
		out.println(i + " ");
	}
%>] ← %스크립트릿 | JSTL→ [ 
<c:forEach var = "i" items="${myList}">
	${i} 
</c:forEach>
]
</body>
</html>