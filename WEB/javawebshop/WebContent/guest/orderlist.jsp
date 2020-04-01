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
<title>주문 목록</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="../js/script.js"></script>
<style type="text/css">
	 h2 a:link { text-decoration: none;}
	 h2 a:visited {text-decoration: none;}
	 h2 a:hover {text-decoration: none;}
</style>
</head>
<body>
<h2 style="margin:30px; text-align: center;"><a href="guest_index.jsp" > 전문 쇼핑몰 </a></h2>
<%@include file="guest_top.jsp" %>

<div style="margin:30px;">
	<table style="width:80%; margin-left:10%;">
		<tr class="table-primary"><th colspan="5" style="text-align: center;"> 주문 상품 목록 </th></tr>
		<tr>
			<th>주문 번호</th><th>상품명</th><th>주문 수량</th><th>주문 일자</th><th>주문 상태</th>
		</tr>
		<%
			String id = (String)session.getAttribute("idKey");
			ArrayList<OrderDto> list = orderMgr.getOrder(id);
			
			if(list.size() == 0){		
		
		%>
			<tr><td colspan="5" style="text-align: center;">주문한 상품이 없습니다</td></tr>
		<%
			}else{
				for(OrderDto ord:list){
					ProductDto productDto = productMgr.getProduct(ord.getProduct_no()); //상품의 이름을 가져오기 위해서
			%>
				<tr>
					<td><%=ord.getNo() %></td>
					<td><%=productDto.getName() %></td>
					<td><%=ord.getQuantity() %></td>
					<td><%=ord.getSdate() %></td>
					<td>
						<%
							switch(ord.getState()){
								case "1": out.print("접수 완료"); break;
								case "2": out.print("입금확인"); break;
								case "3": out.print("배송준비"); break;
								case "4": out.print("배송중"); break;
								case "5": out.print("처리완료"); break;
								default:  out.print("접수중");
							}
						%>
					</td>
				</tr>
			<%
				}
			}
		%>
	</table>
</div>

<%@include file="guest_bottom.jsp" %>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>