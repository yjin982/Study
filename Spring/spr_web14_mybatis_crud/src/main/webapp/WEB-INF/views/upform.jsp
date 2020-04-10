<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3</title>
</head>
<body>
<h3>회원 자료 수정</h3>
<form action="update" method="post">
번호 : ${dto.num} 
		<input type="hidden" name="num" value="${dto.num}"><p/>
이름 : <input type="text" name="name" value="${dto.name}"><p/>
주소 : <input type="text" name="addr" value="${dto.addr}" size="50"><p/>
<input type="submit" value="수정"><p/>
</form>
</body>
</html>