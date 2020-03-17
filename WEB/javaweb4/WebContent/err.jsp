<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
    isErrorPage="true"
    %>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
에러 발생! <br> <!-- 지시어에 isErrorPage true로 해주면 exception이 사용 가능(기본은 false) -->
<!-- 에러 발생해서 이 파일이 보여도 주소상에서는 에러발생 페이지주소로 보여짐 = 서버가 서버파일을 요청해서 => 리다이렉트or포워드 -->
<%=exception.getMessage() %>
</body>
</html>