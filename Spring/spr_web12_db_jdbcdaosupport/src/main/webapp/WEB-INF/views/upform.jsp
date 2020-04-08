<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>5</title>
</head>
<body>
<h2>자료 수정</h2>
<form action="update" method="post">
	id : ${updata.id} <input type="hidden" name="id" value="${updata.id}"><p/>
	pw : <input type="text" name="passwd" value="${updata.passwd}"><p/>
	name : <input type="text" name="name" value="${updata.name}"><p/>
	<input type="submit" value="수정 완료">
</form>
</body>
</html>