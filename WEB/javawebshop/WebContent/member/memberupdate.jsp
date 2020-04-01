<%@page import="pack.member.MemberBean"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr"></jsp:useBean>
<jsp:useBean id="memberDto" class="pack.member.MemberBean"></jsp:useBean>
<% 
	request.setCharacterEncoding("utf-8");
	String id = (String)session.getAttribute("idKey");
	
	MemberBean bean = memberMgr.getMember(id);
	
	if(bean == null){
		response.sendRedirect("../guest/guest_index.jsp");
		return;
	}
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원 수정</title>

<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="../js/script.js"></script>
<script type="text/javascript">
window.onload = function(){
	///...
	
}
</script>
</head>
<body>
<br>
<form action="memberupdateproc.jsp" name="updateFrom" method="post">
<table class="table table-borderless">
	<tr>
		<td colspan="2" align="center" >
			<b><%=bean.getName() %></b>회원님의 정보를 수정합니다.
		</td>
	</tr>
	<tr><td colspan="2" align="center" >
	<table border="1" style="width: 50%;" class="table table-hover">
		<tr>
			<td>아이디</td>
			<td><%=bean.getId() %></td>
		</tr>
		<tr>
			<td>비밀번호</td>
			<td><input type="text" name="passwd" value="<%=bean.getPasswd() %>" /></td>
		</tr>
		<tr>
			<td>이름</td>
			<td><input type="text" name="name" value="<%=bean.getName() %>" /></td>
		</tr>
		<tr>
			<td>이메일</td>
			<td><input type="text" name="email" value="<%=bean.getEmail() %>" /></td>
		</tr>
		<tr>
			<td>전화번호</td>
			<td><input type="text" name="phone" value="<%=bean.getPhone() %>" /></td>
		</tr>
		<tr>
			<td>우편번호</td>
			<td><input type="text" name="zipcode" value="<%=bean.getZipcode() %>" /></td>
		</tr>
		<tr>
			<td>주소</td>
			<td><input type="text" name="address" value="<%=bean.getAddress()%>" /></td>
		</tr>
		<tr>
			<td>직업</td>
			<td>
				<select name=job>
					<option value="<%=bean.getJob() %>"><%=bean.getJob() %></option>
					<option value="회사원">회사원</option>
					<option value="학생">학생</option>
					<option value="자영업">자영업</option>
					<option value="주부">주부</option>
					<option value="기타">기타</option>
				</select>
			</td>
		</tr>
		<tr>
			<td colspan="2" style="text-align: center;">
				<input type="submit" value="수정하기" > &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
				<input type="button" value="수정취소" onclick="javascript:history.back()">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
				<input type="button" value="회원탈퇴" >
			</td>
		</tr>
	</table>
	</td></tr>
</table>
</form>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>