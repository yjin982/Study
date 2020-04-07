<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>1</title>
</head>
<body>
요청 파라미터 연습<p/>
<a href="kbs/login?type=admin">관리자</a> 
<a href="kbs/login?type=user">일반인</a>  
<a href="kbs/login">파라미터 없음</a> <p/>

<form action="kbs/login" method="post">
	data : <input type="text" name="type"> 
	<input type="submit" value="전송1">
</form><p/>
<form action="kbs/korea" method="post">
	data : <input type="text" name="type"> 
	<input type="submit" value="전송2">
</form><p/>
<form action="kbs/asia" method="post">
	data : <input type="text" name="type"> 
	<input type="submit" value="전송3">
</form><p/>
<hr>
<form action="ent/sm/singer/redvelvet">
	선곡 : <input type="text" name="title" value="음파음파">
	<input type="submit" value="전송">
</form><p/>
<form action="ent/jyp/singer/twice">
	선곡 : <input type="text" name="title" value="BDZ">
	<input type="submit" value="전송">
</form><p/>
</body>
</html>