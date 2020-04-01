<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="orderBean" class="pack.order.OrderBean"></jsp:useBean>
<jsp:setProperty property="*" name="orderBean"/>
<jsp:useBean id="cartMgr" class="pack.order.CartMgr" scope="session"></jsp:useBean> <!-- 세션이 살아있는 동안만 유효한 빈 -->
<%
	String flag = request.getParameter("flag"); //구매목록 추가, 수정, 삭제 판단용
	String id = (String)session.getAttribute("idKey");
	//out.print("주문 수량 : " + orderBean.getProduct_no() + orderBean.getQuantity());
	
	
	if(id == null){
		response.sendRedirect("../member/login.jsp"); //고객 로그인 안한 경우, 로그인으로 이동
	}else{
		if(flag == null){//구매 목록 추가
			orderBean.setId(id);
			cartMgr.addCart(orderBean); //카트에 주문 상품 담기
		%>
			<script>
				alert("장바구니에 담기 성공!");
				location.href="cartlist.jsp"; //장바구니 목록 페이지로 이동(상품페이지로 이동하기로 하는게 더 좋음)
			</script>			
		<%			
		}else if(flag.equals("update")){ //구매목록 수정
			orderBean.setId(id);
			cartMgr.updateCart(orderBean);
		%>
			<script>
				alert("장바구니 수정 성공!");
				location.href="cartlist.jsp";
			</script>			
		<%
		}else if(flag.equals("del")){//구매목록 삭제
			orderBean.setId(id);
			cartMgr.deleteCart(orderBean);
		%>
			<script>
				alert("해당 상품의 주문을 삭제했습니다!");
				location.href="cartlist.jsp";
			</script>			
		<%
		}
	}

%>