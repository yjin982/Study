<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
	String num = request.getParameter("num");
	String spage = request.getParameter("page");
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">

<script type="text/javascript">
function check(){
	if(frm.pass.value === ""){
		alert("비밀번호 입력!");
		frm.pass.foucs();
		return;
	}
	
	if(confirm("정말 삭제할까요?")){
		frm.submit();
	}
}
</script>
</head>
<body>
<h2> 글 삭제 </h2>
<form action="deleteok.jsp" name="frm" method="post">
	<input type="hidden" name="num" value="<%=num%>">
	<input type="hidden" name="page" value="<%=spage%>">
	비밀번호 입력 : <input type="password" name="pass"><br><br>
	<input type="button" value="삭제 확인" onclick="check()">&nbsp;
	<input type="button" value="목록 보기" onclick="location.href='boardlist.jsp?page=<%=spage %>'"><p/>
</form>
</body>
</html>