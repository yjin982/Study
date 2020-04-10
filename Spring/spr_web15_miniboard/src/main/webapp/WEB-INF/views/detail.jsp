<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>3</title>
<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnList").onclick = () => {
		location.href="boardlist";
	}
	document.getElementById("btnUpdate").onclick = () => {
		if(confirm("수정하시겠습니까?")){
			frm.action = "upfrm";
			frm.submit(); //POST
		}
	}
	document.getElementById("btnDelete").onclick = () => {
		if(confirm("삭제하시겠습니까?")){
			frm.action = "delete";
			frm.submit();
		}
	}
}
</script>
</head>
<body>
<h3>글 보기</h3>
<form name="frm" method="post">
글 번호 : ${data.num}<input type="hidden" name="num" value="${data.num }"><p/>
작성자 : ${data.author }<input type="hidden" name="author" value="${data.author }"><p/>
글제목 : ${data.title }<input type="hidden" name="title" value="${data.title }"><p/>
글내용 : ${data.content }<input type="hidden" name="content" value="${data.content }"><p/>
<br><br>
작성일 : ${data.bwrite }<input type="hidden" name="bwrite" value="${data.bwrite }"><p/>
조회수 : ${data.readcnt } <input type="hidden" name="readcnt" value="${data.readcnt }"><p/>
<input type="button" value="목록" id="btnList"> 
<input type="button" value="수정" id="btnUpdate"> 
</form>
</body>
</html>