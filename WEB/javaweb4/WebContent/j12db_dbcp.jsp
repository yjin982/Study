<%@page import="pack.SangpumDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="connBeanPooling" class="pack.ConnBeanPooling"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
<title>Insert title here</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/css/bootstrap.min.css" integrity="sha384-MCw98/SFnGE8fJT3GXwEOngsV7Zt27NXFoaoApmYm81iuXoPkFOJwJ8ERdknLPMO" crossorigin="anonymous">
<script type="text/javascript">
	function funcUp() {
		var code = prompt("수정할 코드 입력");
		if(code != "" && code != null)
			location.href="j12up.jsp?code=" + code;
	}
	
	function funcDel() {
		var code = prompt("삭제할 코드 입력");
		if(code != "" && code != null)
			if(confirm("정말 삭제할까요?") == true)
				location.href="j12del.jsp?code=" + code;
	}
</script>
</head>
<body>
<script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.3/js/bootstrap.min.js" integrity="sha384-ChfqqxuZUCnJSK3+MXmPNIyE6ZbWh2IMqE241rYiqJxyMiZ6OW/JmZQ5stwEULTy" crossorigin="anonymous"></script>
<h2>* 상품자료(jsp:Beans + DBCP) *</h2>
<a href="j12ins.html">추가</a>&nbsp;
<a href="javascript:funcUp()">수정</a>&nbsp;
<a href="javascript:funcDel()">삭제</a>&nbsp;<p/>

<!--<table border="1" style="border-collapse: collapse;"> -->
<table class="table table-bordered" style="width: 40%;">
	<tr class="table-primary">
		<th scope="col">code</th><th scope="col">sang</th><th scope="col">su</th><th scope="col">dan</th>
	</tr>
	<% //j7db.jsp와 비교 / 현재로써 이 부분 자바는 어쩔수없다 => EL로 해결
		ArrayList<SangpumDto> list = connBeanPooling.getDataAll();
		for(SangpumDto s:list){
	%>
	<tr class="table-light">
		<td scope="row"><%=s.getCode() %></td>
		<td><%=s.getSang() %></td>
		<td><%=s.getSu() %></td>
		<td><%=s.getDan() %></td>
	</tr>
	<%
		}
	%>
</table>
</body>
</html>