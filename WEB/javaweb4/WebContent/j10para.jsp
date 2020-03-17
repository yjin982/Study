<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<% request.setCharacterEncoding("utf-8"); %>
<jsp:useBean id="bean" class="pack.ExamBean"></jsp:useBean>
<jsp:useBean id="examProcess" class="pack.ExamProcess"></jsp:useBean>

<jsp:setProperty property="*" name="bean"/> <!-- formBean으로 변수 여러개 set할때 -->
<jsp:setProperty property="examBean" name="examProcess" value="<%=bean %>"/> <!-- property 값으로 setter 가 세팅되어있다는 것 -->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%--<%=bean.getName() + " " + bean.getKor() + " " + bean.getEng()--%>
성적 자료 출력<br>

이름은 <jsp:getProperty property="name" name="bean"/><br>
국어 : <jsp:getProperty property="kor" name="bean"/><br>
영어 : <jsp:getProperty property="eng" name="bean"/><br><br>

총점 : <jsp:getProperty property="tot" name="examProcess"/><br>
평균 : <jsp:getProperty property="avg" name="examProcess"/><br>
</body>
</html>