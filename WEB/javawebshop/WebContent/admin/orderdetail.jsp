<%@page import="pack.product.ProductDto"%>
<%@page import="pack.order.OrderDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="orderMgr" class="pack.order.OrderMgr"></jsp:useBean>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr"></jsp:useBean>
<%
	OrderDto orderDto = orderMgr.getOrderDetail(request.getParameter("no"));
	ProductDto productDto = productMgr.getProduct(orderDto.getProduct_no());
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>주문 상세보기 - 관리자</title>
<link href="../css/board.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="../js/script.js"></script>
</head>
<body>
<%@ include file="admin_top.jsp" %>
<p style="text-align: center;">주문 상세 보기</p>
<form action="orderproc_admin.jsp" name="detailFrm" method="post">
	<table border="1" style="width: 80%; text-align: center; border-collapse: collapse;">
		<tr>
	 		<th>고객 아이디</th><td><%=orderDto.getId() %></td>
	 		<th>주 문 번 호</th><td><%=orderDto.getNo() %></td>
	 		<th>상 품 번 호</th><td><%=orderDto.getProduct_no() %></td>
	 		<th>상 품 명</th><td><%=productDto.getName() %></td>
	 	</tr>
	 	<tr>
	 		<th>상 품 가 격</th><td><%=productDto.getPrice() %></td>
	 		<th>주 문 수 량</th><td><%=orderDto.getQuantity() %></td>
	 		<th>재 고 수 량</th><td><%=productDto.getStock() %></td>
	 		<th>주 문 일 자</th><td><%=orderDto.getSdate() %></td>
	 	</tr>
	 	<tr>
	 		<th colspan="4" style="text-align:center;" height="40">결제 금액</th>
	 		<td colspan="4"><%=Integer.parseInt(orderDto.getQuantity()) * Integer.parseInt(productDto.getPrice()) %></td>
	 	</tr>
	 	<tr>
	 		<th colspan="4" style="text-align: center;" height="100">주문 상태</th>
	 		<td colspan="4" >
	 		<select name="state">
	 				<option value="1">접수</option>
	 				<option value="2">입금확인</option>
	 				<option value="3">배송 준비</option>
	 				<option value="4">배송 중</option>
	 				<option value="5">처리 완료</option>
	 			</select>
	 			<script type="text/javascript">
	 				document.detailFrm.state.value = <%=orderDto.getState() %>
	 			</script>
	 		</td>
	 	</tr>
	 	<tr>
	 		<td colspan="8" style="text-align: center;" height="40">
	 			<input type="button" value="수 정" onclick="orderUpdate(this.form)"> / 
	 			<input type="button" value="삭 제" onclick="orderDelete(this.form)">
	 			<input type="hidden" name="no" value="<%=orderDto.getNo() %>">
	 			<input type="hidden" name="flag">
	 		</td>
	 	</tr>
	</table>
</form>
<%@ include file="admin_bottom.jsp" %>
</body>
</html>