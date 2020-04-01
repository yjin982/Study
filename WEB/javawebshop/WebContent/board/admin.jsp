<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<script type="text/javascript">
function chk(){
	if(frm.id.value == "" || frm.pwd.value == ""){
		alert("아이디 혹은 비밀번호를 입력하시오");
		return;
	}
	frm.submit();
}

</script>
</head>
<body>
<form action="adminlogin.jsp" name="frm" method="post">
<table style="width: 100%">
	<tr>
		<td>
		<%
			String sessionVal = (String)session.getAttribute("adminKey");
			if(sessionVal != null){
		%>
			이미 로그인 했어요<br><br>
			[ <a href="adminlogout.jsp">로그아웃</a> ] [ <a href="javascript:window.close()">창닫기</a> ]
		<%
			}else{
		%>
			<table style="width: 100%">
				<tr><td>i&nbsp;&nbsp;&nbsp;d : <input type="text" name="id"></td></tr>
				<tr><td>pwd : <input type="text" name="pwd"></td></tr>
				<tr>
					<td>[ <a href="#" onclick="chk()">로그인</a> ] [ <a href="javascript:window.close()">창닫기</a> ]</td>
				</tr>
			</table>
		<%		
			}
		%>
		</td>
	</tr>
</table>
</form>


</html>