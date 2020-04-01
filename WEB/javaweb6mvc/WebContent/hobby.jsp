<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>mvc-2</title>
</head>
<body>
취미 선택 결과<br>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<c:forEach var="h" items="${datas}">
	${h} &nbsp;&nbsp;&nbsp;
</c:forEach>




<!-- web.xml 에 이렇게 추가하거나 어노테이션을 쓰거나
  <servlet>
  	<servlet-name>mvc</servlet-name>
  	<servlet-class>pack.HobbyController</servlet-class>
  </servlet>
  <servlet-mapping>
  	<servlet-name>mvc</servlet-name>
  	<url-pattern>*.do</url-pattern>
  </servlet-mapping>
   -->
</body>
</html>