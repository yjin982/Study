<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"
	isELIgnored="false"    
%><!--EL관련 지시어 isELIgnored 기본은 false(=기본으로 지원함)-->
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>2</title>
</head>
<body>
EL 연습 : 연산자, 내장 객체 <br>
---------------------------------<br>
연산자 사용<br>
\${3 + 4 } --> ${3 + 4 }<br>
\${5 / 4 }, \${5 div 4 } --> ${5 / 4 }, ${5 div 4 } | 이클립스에서 div 에러처리하지만 실제는 에러가 아님<br>
\${5 / 0 } --> ${5 / 0 }  | 에러X, Infinity<br>
\${5 % 4 }, \${5 mod 4 } --> ${5 % 4 }, ${5 mod 4 }<br> 
\${5 >= 4} ge --> ${5 >= 4 } greater <br>
\${5 le 0 } --> ${5 le 0 } less <br>
\${5 > 4 and 3 gt 2} --> ${5 > 4 and 3 gt 2}<br>
\${5 > 4 ? 10 : 20*2} --> ${5 > 4 ? 10 : 20*2}<br>
 <br>
 내장객체 사용<br>
 <%
 	request.setAttribute("aa", "air");
 	session.setAttribute("bb",	 "book");
 	application.setAttribute("cc", "cat");
 %>
 표현식 &nbsp;&nbsp; EL<br>
 <%=request.getAttribute("aa") %> &nbsp; ${requestScope.aa } <br>
 <%=session.getAttribute("bb") %> &nbsp; ${sessionScope.bb } <br>
 <%=application.getAttribute("cc") %> &nbsp; ${applicationScope.cc } <br>
<br>
jsp의 내장 객체 : <%=request.getHeader("host") %><br>
el의 내장 객체 : ${header.host } 또는 ${header["host"]}<br>
<br>
html 문서 자료 받기 <br>
<a href="eltest.html">자료 얻기</a><br>
이름 : ${param.irum } 또는 ${param["irum"]} <br>
성격 : ${paramValues.sung[0]}, ${paramValues.sung[1]}
</body>
</html>