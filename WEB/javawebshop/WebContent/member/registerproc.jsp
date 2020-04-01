<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
    
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="memberBean" class="pack.member.MemberBean"></jsp:useBean>
<jsp:setProperty property="*" name="memberBean"/>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr"></jsp:useBean>
<%
	boolean b = memberMgr.memberInsert(memberBean);
	
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>회원가입</title>
</head>
<body>
<br><br>
<div style="text-align: center; font-size: 1.2em;">
	<%
		if(b){
	%>
		회원 가입을 축하합니다! <br>
		<a href="../index.jsp">메인으로</a>
	<%
		}else{
	%>
		회원 가입 실패! 관리자에게 문의하기 바랍니다.<br>
		<a href="register.jsp">가입 재시도</a>	
	<%
		}
	%>
</div>
</body>
</html>