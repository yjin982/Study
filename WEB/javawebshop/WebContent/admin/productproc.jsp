<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!--  controller 역할 : insert, update, delete -->
<jsp:useBean id="productMgr" class="pack.product.ProductMgr" />
<%
String flag = request.getParameter("flag");

boolean result = false;

if(flag.equals("insert")) { //추가
	result = productMgr.insertProduct(request);
} else if(flag.equals("update")) { //수정
	result = productMgr.updateProduct(request);
} else if(flag.equals("delete")) { //삭제
	result = productMgr.deleteProduct(request.getParameter("no"));
} else {
	response.sendRedirect("productmanager.jsp");
}

if(result) {
%>
	<script>
		alert('정상 처리');
		location.href="productmanager.jsp";
	</script>
<%
} else {
%>
	<script>
		alert('오류 발상\n관리자에게 문의 바람');
		location.href="productmanager.jsp";
	</script>
<%	
}
%>