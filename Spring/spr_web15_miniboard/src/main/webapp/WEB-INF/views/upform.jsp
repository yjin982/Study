<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>4</title>
<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnList").onclick = () => {
		location.href="boardlist";
	}
	document.getElementById("btnUpdate").onclick = () => {
		frm.action = "update";
		frm.submit();
	}
}
</script>
</head>
<body>
<h3>글 수정</h3>
<form name="frm" method="post">
글 번호 : ${data.num}<input type="hidden" name="num" value="${data.num }"><p/>
작성자 : <input type="text" name="author" value="${data.author }"><p/>
글제목 : <input type="text" name="title" value="${data.title }"><p/>
글내용 : <textarea rows="5" cols="30" name="content">${data.content }</textarea><p/>
<br><br>
작성일 : ${data.bwrite }<p/>
조회수 : ${data.readcnt } <p/>
<input type="button" value="목록" id="btnList"> 
<input type="button" value="수정" id="btnUpdate"> 
</form>
</body>
</html>