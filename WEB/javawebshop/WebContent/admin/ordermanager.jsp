<%@page import="pack.product.ProductDto"%>
<%@page import="pack.order.OrderDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="orderMgr" class="pack.order.OrderMgr"></jsp:useBean>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>주문 관리 - 관리자</title>
<link href="../css/board.css" rel="stylesheet" type="text/css">
<script type="text/javascript" src="../js/script.js"></script>
</head>
<body>
<%@ include file="admin_top.jsp" %>
<p style="text-align: center;">주문된 전체 상품 목록</p>
<table style="width: 80%;">
 	<tr>
 		<th>주문번호</th><th>주문id</th><th>상품명</th><th>주문 수</th><th>주문일자</th><th>주문상태</th><th>보기</th>
 	</tr>
 	<%
 		ArrayList<OrderDto> list = orderMgr.getOrderAll();
 		
 		if(list.size() == 0){
	 	%>
	 	<tr><td colspan="7" style="text-align: center;">주문된 상품이 없습니다</td></tr>
	 	<%
 		}else{
 			for(int i=0; i < list.size(); i++){
 				OrderDto orderDto = (OrderDto)list.get(i);
 				ProductDto productDto = productMgr.getProduct(orderDto.getProduct_no());
		 	%>
			<tr>
				<td><%=orderDto.getNo() %></td>
				<td><%=orderDto.getId() %></td>
				<td><%=productDto.getName() %></td>
				<td><%=orderDto.getQuantity() %></td>
				<td><%=orderDto.getSdate() %></td>
				<td>
					<%
						switch(orderDto.getState()){
							case "1": out.print("접수 완료"); break;
							case "2": out.print("입금확인"); break;
							case "3": out.print("배송준비"); break;
							case "4": out.print("배송중"); break;
							case "5": out.print("처리완료"); break;
							default:  out.print("접수중");
						}
					%>
				</td>
				<td>
					<a href="javascript:orderDetail('<%=orderDto.getNo() %>')" >상세보기</a>
				</td>
			</tr>
			<%
 			}
		} 
	%>
</table>
<%@ include file="admin_bottom.jsp" %>

<form action="orderdetail.jsp" name="detailFrm" method="post">
	<input type="hidden" name="no">
</form>
</body>
</body>
</html>