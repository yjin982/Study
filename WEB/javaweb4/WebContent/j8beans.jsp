<%@page import="pack.Gugudan"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<% int dan = Integer.parseInt(request.getParameter("dan")); %>
<%=dan + "단 출력<br>" %>
<hr>
** 현재 실력으로 구구단 출력 ** <br>
<%
	//Gugudan gugudan = new Gugudan(); //클래스의 포함, 클라이언트 갯수만큼 new를 하는 비효율성
	Gugudan gugudan = Gugudan.getInstance(); // 싱글톤으로 클래스 포함관계 구현
	int re[] = gugudan.computeGugu(dan);
	for(int i = 0; i < 9; i++){
		out.println(dan + " * " + (i+1) + " = " + re[i] + "&nbsp;&nbsp;");
	}
%>
<hr>
** Beans로 구구단 출력 ** <br>
<jsp:useBean id="gugu" class="pack.Gugudan" scope="page"></jsp:useBean> <!-- Gugudan gugu = new Gugudan(); 과 같은 효과 -->
<!-- scope 현재 빈즈가 영향받는 범위(application, page, request, session  -->
<% 
	int re2[] = gugu.computeGugu(dan);
	for(int i = 0; i < 9; i++){
		out.println(dan + " * " + (i+1) + " = " + re2[i] + "&nbsp;&nbsp;");
	}	
%>
</body>
</html>