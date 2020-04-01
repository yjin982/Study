<%@page import="pack.product.ProductDto"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr"></jsp:useBean>
<%
	String no = request.getParameter("no");
	ProductDto dto = productMgr.getProduct(no);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>상품 상세보기 - 고객</title>
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
<div style="text-align: center;">고객님 지갑을 마음껏 열어주세요~ - 상세보기 페이지</div>

<div style="margin:30px;">
	<form action="cartproc.jsp">
		<table style="width:80%; margin-left:10%;">
			<tr>
				<th colspan="3">상품 상세 보기</th>
			</tr>
			<tr>
				<td style="width: 20%">
					<img src="../upload/<%=dto.getImage() %>" width="150px;">
				</td>
				<td style="width: 50%; vertical-align: top;">
					<table style="width: 100%;">
						<tr>
							<td>번호</td>	<td><%=dto.getNo() %></td>
						</tr>
						<tr>
							<td>품명</td>	<td><%=dto.getName() %></td>
						</tr>
						<tr>
							<td>가격</td>	<td><%=dto.getPrice() %></td>
						</tr>
						<tr>
							<td>등록</td>	<td><%=dto.getSdate() %></td>
						</tr>
						<tr>
							<td>재고</td>	<td><%=dto.getStock() %></td>
						</tr>
						<tr>
							<td>주문 수량</td>
							<td>
								<input type="text" name="quantity" value="1" size="5" style="text-align: center;">
							</td>
						</tr>
					</table>
				</td>
				<td style="vertical-align: top;">
					<b>상품 설명</b><br>
					<%=dto.getDetail() %>
				</td>
			</tr>
			<tr>
				<td colspan="3" style="text-align: center;">
					<input type="hidden"" name="product_no" value="<%=dto.getNo() %>">
					<input type="submit" value="장바구니에 담기">&nbsp;&nbsp;
					<input type="button" value="뒤로가기" onclick="history.back()">
				</td>
			</tr>
		</table>
	</form>
</div>



<%@include file="guest_bottom.jsp" %>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>