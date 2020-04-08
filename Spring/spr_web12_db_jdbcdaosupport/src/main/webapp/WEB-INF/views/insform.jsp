<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="sform" uri="http://www.springframework.org/tags/form" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3</title>
</head>
<body>
<h2>자료 추가</h2>
<sform:form modelAttribute="command">
	아이디 : <sform:input path="id"/><p/>
	비밀번호 : <sform:input path="passwd"/><p/>
	이름 : <sform:input path="name"/><p/>
	<input type="submit" value="추가">
</sform:form>
</body>
</html>