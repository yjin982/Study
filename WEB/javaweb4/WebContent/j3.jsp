<%@ page language="java" contentType="text/html; charset=UTF-8" import="java.util.Date"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>include</title>
</head>
<body>
<%@ include file="top.jsp" %> <!-- 지시어로 include -->
<h1>파일의 포함(include)</h1>
어쩌구 저쩌구<br> 블라블라 <br><br>
↓ 액션태그 ↓ <br>
<jsp:include page="action1.jsp"></jsp:include> <!-- 액션태그 -->
<br>
<div style="color:#A0A8FF;">
	<jsp:include page="action2.jsp">
		<jsp:param value="korea" name="msg"/>
	</jsp:include>
</div>
<br>↑ 액션태그 ↑<br>
<%@ include file="bottom.jsp" %> <!-- bottom.jsp 소스를 여기로 불러와서 포함시켜서 실행시킴 -->
</body>
</html>