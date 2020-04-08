<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="stag" uri="http://www.springframework.org/tags" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3</title>
</head>
<body>
결과 : ${msg} <p/>
<stag:message code="show.disp" /> : ${msg}
</body>
</html>