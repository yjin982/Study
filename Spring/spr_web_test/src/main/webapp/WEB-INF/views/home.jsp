<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@ page session="false" %>
<html>
<head>
	<title>Home</title>
</head>
<body>
<h1>
	Hello world!  
</h1>

<P>  The time on the server is ${serverTime}. </P>
<p><a href="sub1">sub1</a></p> 
<p>
	<a href="sub2?irum=tom">sub2</a>-para  
	<a href="sub2?irum=oscar">sub2</a>-para
</p>
 <p>
 	<img src="./resources/images/pic.jpg" width="300px">
 </p>

</body>
</html>
