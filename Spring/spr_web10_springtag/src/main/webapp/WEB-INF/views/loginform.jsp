<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="sform" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
<h2>자료 입력(Spring tag)</h2>
<sform:form commandName="command">
	id : <sform:input path="userid"/> &nbsp; <sform:errors path="userid" /><p/>
	pw : <sform:input path="passwd"/> &nbsp; <sform:errors path="passwd" /><p/>
	<input type="submit" value="전송">
</sform:form>
<hr>
같은 기능
<form id="command" action="/cc/login" method="post">
	id : <input id="userid" name="userid" type="text" value=""/><p/>
	pw : <input id="passwd" name="passwd" type="text" value=""/><p/>
	<input type="submit" value="전송">
</form>

</body>
</html>