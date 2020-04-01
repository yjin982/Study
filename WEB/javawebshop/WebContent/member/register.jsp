<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원가입</title>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="../js/script.js"></script>
<script type="text/javascript">
window.onload = function(){
	regForm.id.focus();
	document.getElementById("btnZip").onclick = zipCheck;
	document.getElementById("btnId").onclick = idCheck;
	document.getElementById("btnSubmit").onclick = inputCheck;
}
</script>
</head>
<body>
<br>
<table class="table table-borderless">
<tr>
	<td align="center" valign="middle" >
		<form name="regForm" method="post" action="registerproc.jsp">
			<table border="1" >
				<tr align="center" style="background-color: #C4DEFF;">
					<td colspan="2"><b style="color: #FFFFFF;">회원 가입</b></td>
				</tr>
				<tr>
					<td width="16%">아이디</td>
					<td width="57%"><input type="text" name="id" size="15">
						<input type="button" value="ID중복확인" id="btnId"></td>
				</tr>
				<tr>
					<td>패스워드</td>
					<td><input type="password" name="passwd" size="15"></td>
				</tr>
				<tr>
					<td>패스워드 확인</td>
					<td><input type="password" name="repasswd" size="15"></td>
				</tr>
				<tr>
					<td>이름</td>
					<td><input type="text" name="name" size="15"></td>
				</tr>
				<tr>
					<td>이메일</td>
					<td><input type="text" name="email" size="27"></td>
				</tr>
				<tr>
					<td>전화번호</td>
					<td><input type="text" name="phone" size="20"></td>
				</tr>
				<tr>
					<td>우편번호</td>
					<td>
						<input type="text" name="zipcode" size="7"> 
						<input type="button" value="우편번호찾기" id="btnZip">
					</td>
				</tr>
				<tr>
					<td>주소</td>
					<td><input type="text" name="address" size="60"></td>
				</tr>
				<tr>
					<td>직업</td>
					<td>
						<select name=job>
							<option value="0">선택하세요</option>
							<option value="회사원">회사원</option>
							<option value="학생">학생</option>
							<option value="자영업">자영업</option>
							<option value="주부">주부</option>
							<option value="기타">기타</option>
						</select>
					</td>
				</tr>
				<tr>
					<td colspan="2" align="center">
						<input type="button" value="회원가입" id="btnSubmit">	&nbsp;&nbsp;&nbsp;&nbsp;
						<input type="reset" value="다시쓰기">&nbsp;&nbsp;&nbsp;&nbsp;  
						<input type="button" value="뒤로가기" onclick="javascript:history.go(-1)">
					</td>
				</tr>
			</table>
		</form>
	</td>
</tr>
</table>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>