<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr" scope="page"></jsp:useBean>
<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id"); 
	
	boolean b = memberMgr.checkId(id);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>아이디 체크</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
</head>
<body>
<br><br>
<div style="text-align: center; font-size: 1.2em;">
	<b><%=id %></b>&nbsp;
	<%
		if(b){
	%>
		는 이미 사용 중인 아이디 입니다.<p/>
		<a href="#" onclick="opener.document.regForm.id.focus(); window.close();">닫기</a>
	<%
		}else{
	%>
		는 사용 가능한 아이디 입니다.<p/>
		<a href="#" onclick="opener.document.regForm.passwd.focus(); window.close();">닫기</a>
	<%		
		}
	%>
</div>
</body>
</html>