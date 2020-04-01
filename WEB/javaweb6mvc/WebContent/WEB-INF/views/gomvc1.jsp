<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>mvc-1</title>
</head>
<body>
뷰1의 결과 : <br>
출력1 : <%=request.getAttribute("result") %>____(%를 이용한 전통적인 방법)<br>
출력2 : ${requestScope.result}==${result}____(el을 이용, requestScope생략가능)<br>
</body>
</html>