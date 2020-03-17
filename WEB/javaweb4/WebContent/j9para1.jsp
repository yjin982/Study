<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%
	request.setCharacterEncoding("utf-8");
	String msg = request.getParameter("message");	
%>
<jsp:useBean id="my" class="pack.Para1Class"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
* 클래스 private 멤버 필드에 갑 설정하고 참조하기 *<br>
<b>지금까지의 기술로 작성</b> <br>
<% 
	my.setMessage(msg);
	out.println(my.getMessage());
%>
<p/>
<b>액션태그로 작성</b><br><%-- <jsp:setProperty property="message" name="my"/ value="하.하.하."> --%>
<jsp:setProperty property="message" name="my"/> <!-- Para1Class의 Setter부른 것과 동일 프로퍼티가 msg이면 Setter 이름도 setMsg여야 가능 -->
<jsp:getProperty property="message" name="my"/> <!-- name의 my는 useBean에서 id에 준 값 -->

</body>
</html>