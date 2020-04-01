<%@page import="pack.business.DataDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="memberProcess" class="pack.business.MemberProcess" />
<%
	request.setCharacterEncoding("utf-8");
	String id = request.getParameter("id");
	DataDto dto = memberProcess.selectDataPart(id);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
<h3>** 회원 정보 수정 **</h3>
<form action="upok.jsp" method="post">
	아이디 : <%=dto.getId() %><input type="hidden" name="id" value="<%=dto.getId() %>"><br>
	작성자 : <input type="text" name="name" value="<%=dto.getName() %>"><br>
	비밀번  : <input type="text" name="passwd" > 비밀번호 불일치 시 수정 불가<br>
	 <br>
	 <input type="submit" value="수정">
</form>
</body>
</html>