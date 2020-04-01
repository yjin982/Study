<%@page import="pack.product.ProductDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="productMgr" class="pack.product.ProductMgr"></jsp:useBean>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>상품목록 - 고객</title>
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="../js/script.js"></script>
<style type="text/css">
	 h2 a:link { text-decoration: none;}
	 h2 a:visited {text-decoration: none;}
	 h2 a:hover {text-decoration: none;}
</style>
</head>
<body>
<h2 style="margin:30px; text-align: center;"><a href="guest_index.jsp"> 전문 쇼핑몰 </a></h2>
<%@include file="guest_top.jsp" %>
<div style="text-align: center;">고객님 지갑을 마음껏 열어주세요~</div>
<div style="margin:30px;">
<table style="width:80%; margin-left:10%;">
	<tr>
		<th>상품명</th><th>가격</th><th>재고량</th><th>상세보기</th>
	</tr>
	<%
		ArrayList<ProductDto> list = productMgr.getProductAll();
		for(ProductDto p:list){
	%>
		<tr>
			<td>
				<img src="../upload/<%=p.getImage()%>" width="100">&nbsp;
				<%=p.getName() %>
			</td>
			<td>
				<%=p.getPrice() %>
			</td>
			<td>
				<%=p.getStock() %>
			</td>
			<td>
				<a href="javascript:productDetail('<%=p.getNo()%>')">보기</a>
			</td>
		</tr>	
	<%		
		}
	%>
</table>

<form action="productdetail_g.jsp" name="detailFrm" method="post">
	<input type="hidden" name="no">
</form>
</div>
<%@include file="guest_bottom.jsp" %>
<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>