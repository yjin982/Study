<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>xml-02</title>
</head>
<body>
<h3>자료 입력</h3>
<form action="member" method="post">
	name : <input type="text" name="name"><p/>
	age : <input type="text" name="age"><p/>
	<input type="submit" value="제출"><p/>
</form>
<hr>
<form action="member_xml" method="post">
	name : <input type="text" name="name"><p/>
	age : <input type="text" name="age"><p/>
	<input type="submit" value="제출"><p/>
</form>
</body>
</html>