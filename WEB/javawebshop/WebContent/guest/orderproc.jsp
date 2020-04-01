<%@page import="pack.order.OrderBean"%>
<%@page import="java.util.Enumeration"%>
<%@page import="java.util.Hashtable"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="cartMgr" class="pack.order.CartMgr" scope="session"></jsp:useBean>
<jsp:useBean id="orderMgr" class="pack.order.OrderMgr" scope="page"></jsp:useBean>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr" scope="page"></jsp:useBean> <!-- order에서 주문한 수만큼 재고량이 빠져야하기때문에 사용 -->
<%
	Hashtable hCart = cartMgr.getCartList();
 	Enumeration enu = hCart.keys();
 	
 	if(hCart.size() == 0){ //카트 내역이 없으면
 	%>
 	<script type="text/javascript">
 		alert("주문 내역이 없습니다");
 		location.href="productlist.jsp";
 	</script>
 	<%
 	}else{
 		while(enu.hasMoreElements()){ //shop_order는 추가, shop_product는 빼기
 			OrderBean orderBean = (OrderBean)hCart.get(enu.nextElement());
 			orderMgr.insertOrder(orderBean);       //shop_order(DB)에 주문 정보를 저장
 			productMgr.reduceProduct(orderBean); //주문수량 만큼 shop_product(DB)에 재고량을 빼기
 			cartMgr.deleteCart(orderBean); //주문했으면 카트 삭제
 		}
 	%>
 	<script type="text/javascript">
		alert("주문 처리 성공!");
		location.href="orderlist.jsp";
	</script>	
 	<%
 	}
%>