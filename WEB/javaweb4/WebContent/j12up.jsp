<%@page import="pack.SangpumDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<% String code = request.getParameter("code"); %>
<jsp:useBean id="connBeanPooling" class="pack.ConnBeanPooling"></jsp:useBean>
<% 
	SangpumDto dto = connBeanPooling.updateList(code); 

	if(dto == null){
%>
	<script type="text/javascript">
		alert("등록된 상품 코드가 아닙니다.\n수정 불가");
		location.href="j12db_dbcp.jsp";
	</script>
<%
		return;
	}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
* 상품 수정 * <br>
<form action="j12upok.jsp" method="post">
	코드 : <%=dto.getCode() %><input type="hidden" name="code" id="code" value="<%=dto.getCode() %>"><br>
	품명 : <input type="text" name="sang" id="sang" value="<%=dto.getSang() %>"><br>
	수량 : <input type="text" name="su" id="su" value="<%=dto.getSu() %>"><br>
	단가 : <input type="text" name="dan" id="dan" value="<%=dto.getDan() %>"><br><p/>
	<input type="submit" value="자료수정" >&nbsp; 
	<input type="button" value="목록보기" onclick="javascript:location.href='j12db_dbcp.jsp'">
</form>
</body>
</html>