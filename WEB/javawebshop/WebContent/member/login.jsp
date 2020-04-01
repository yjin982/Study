<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<%
	String id = (String)session.getAttribute("idKey");
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>로그인</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">

<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnLogin").onclick = () => {
		if(loginForm.id.value == ""){
			alert("아이디를 입력하세요");
			loginForm.id.focus();
		}else if(loginForm.passwd.value == ""){
			alert("비밀번호를 입력하세요");
			loginForm.passwd.focus();
		}else{
			loginForm.action="loginproc.jsp";
			loginForm.method = "post";
			loginForm.submit();
		}
	}
	
	document.getElementById("btnNewMember").addEventListener("click", funcNew);
}
function funcNew(){
	location.href="register.jsp";
}
</script>
</head>
<body>

<%
	if(id != null){
%>
<div class="cen">
	<b><%=id %></b>님 환영합니다. <br>
	준비된 기능을 사용할 수 있습니다<br><br>
	<a href="logout.jsp">로그아웃</a>&nbsp;<a href="../index.jsp">메인으로</a>
</div>	
<%	
	}else{
%>
<div class="cen">
	<form name="loginForm">
	<table>
		<thead>
		<tr>
			<td>로그인</td>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>ID</td>
			<td><input type="text" name="id"></td>
		</tr>
		<tr>
			<td>PASSWORD</td>
			<td><input type="password" name="passwd"></td>
		</tr>
		<tr>
			<td colspan="2">
				<input type="button" value="로그인" id="btnLogin">
				<input type="button" value="회원가입" id="btnNewMember">
			</td>
		</tr>
		</tbody>
	</table>
	</form>
</div>
<%		
	}
%>
</body>
</html>