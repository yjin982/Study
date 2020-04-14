<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%@ taglib prefix="form"  uri="http://www.springframework.org/tags/form"%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>파일 업로드 - 02</title>
</head>
<body>
<h3>파일 업로드</h3>
<form:form enctype="multipart/form-data" modelAttribute="uploadFile">
	업로드할 파일 선택 : <input type="file" name="file">
	<form:errors path="file" cssStyle="color:red"/>
	<p/>
	<input type="submit" value="전송">
</form:form>
</body>
</html>