<%@page import="pack.product.ProductDto"%>
<%@page import="pack.order.OrderBean"%>
<%@page import="java.util.Enumeration"%>
<%@page import="java.util.Hashtable"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="cartMgr" class="pack.order.CartMgr" scope="session"></jsp:useBean>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>장바구니</title>
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
		<tr class="table-primary">
			<th>주문 상품명</th><th>가격(소계)</th><th>수량</th><th>수정/삭제</th><th>조회</th>
		</tr>
		<%
			int totalPrice = 0;
			Hashtable hCart = cartMgr.getCartList();
			if(hCart.size() == 0){
		%>
			<tr><td colspan="5" style="text-align: center;">주문 건수가 없습니다.</td></tr>
		<%
			}else{
				Enumeration enu = hCart.keys();
				while(enu.hasMoreElements()){
					OrderBean orderBean = (OrderBean)hCart.get(enu.nextElement());
					ProductDto productDto = productMgr.getProduct(orderBean.getProduct_no());
					int price = Integer.parseInt(productDto.getPrice()); //주문 상품의 낱개 가격
					int quantity = Integer.parseInt(orderBean.getQuantity()); //주문 수량
					int subTotal = price * quantity; //소계
					totalPrice += subTotal; //총계
				%>
				<form action="cartproc.jsp" method="get">
					<input type="hidden" name="flag">
					<input type="hidden" name="product_no" value="<%=productDto.getNo()%>">
					<tr>
						<td><%=productDto.getName() %></td>
						<td><%=subTotal %></td>
						<td><input type="text" style="text-align: center;" name="quantity" size="5" value="<%=orderBean.getQuantity() %>"></td>
						<td>
							<input type="button" value="수정" onclick="cartUpdate(this.form)" class="btn btn-outline-primary">
							<input type="button" value="삭제" onclick="cartDelete(this.form)" class="btn btn-outline-primary">
						</td>
						<td>
							<a class="btn btn-outline-primary" href="javascript:productDetail('<%=productDto.getNo()%>')">상세보기</a>
						</td>
					</tr>
				</form>
				<%	
				}
			}
		%>
		<tr class="table-primary"><td colspan="5">&nbsp;</td></tr>
		<tr><td colspan="3"></td><td><b>총 결제 금액</b></td><td><%=totalPrice %> 원</td></tr>
		<tr><td colspan="4"></td><td><a class="btn btn-outline-primary" href="orderproc.jsp">주문 하기</a></td></tr>
	</table>
</div>

<form action="productdetail_g.jsp" name="detailFrm">
<input type="hidden" name="no">
</form>



<%@include file="guest_bottom.jsp" %>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>