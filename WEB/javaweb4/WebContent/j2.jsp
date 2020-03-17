<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" 
import="java.util.*" import="java.sql.Connection"
session="true"
buffer="16kb"
autoFlush="true"
isThreadSafe="true"
info="jsp 문서 정보"
errorPage="err.jsp"
%>
<%@ page import="java.sql.ResultSet" %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>jsp 지시어</title>
</head>
<body>
<!-- 상단에 있는 %@ page 지시어 : contentType,pageEncoding필수 /  session은 기본값이 true, 생략가능 / buffer 생략가능, 기본 8kb / autoFlush / isThreadSafe / info 파일 정보 / ... 등등 -->
날짜 출력 :
<%
Calendar calendar = Calendar.getInstance();
int year = calendar.get(Calendar.YEAR);
int month = calendar.get(Calendar.MONTH) + 1;
out.println(year + "년 " + month + "월");
%>
<br>
<%=getServletInfo() %>
<hr>
<%= 10/0 %> <!-- 0으로 나누기 불가, 에러 발생시 위 지시어에서 에러페이지로 이동하게 가능 -->
</body>
</html>