<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3</title>
</head>
<body>
<h3>글 쓰기</h3>
<form action="insert" method="post">
<table border="1" cellpadding="5" style="border-collapse: collapse;">
	<tr>
		<td>글 제목</td>
		<td><input type="text" name="title"></td>
	</tr>
	<tr>
		<td>작성자</td>
		<td><input type="text" name="author"></td>
	</tr>
	<tr>
		<td>글 내용</td>
		<td><textarea rows="5" cols="30" name="content"></textarea></td>
	</tr>
	<tr><td colspan="2"><input type="submit" value="글쓰기"></td></tr>
</table>

</form>
</body>
</html>