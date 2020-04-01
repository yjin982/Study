<%@page import="pack.member.ZipCodeDto"%>
<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="memberMgr" class="pack.member.MemberMgr" scope="page"></jsp:useBean>
<%
	request.setCharacterEncoding("utf-8");
	String check = request.getParameter("check"); 
	String dongName = request.getParameter("dongName"); 
	
	ArrayList<ZipCodeDto> list = memberMgr.zipcodeRead(dongName);
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>우편번호 검색</title>
<link href="../css/style.css" rel="stylesheet" type="text/css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script src="../js/script.js"></script>
<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnZipFind").onclick = dongCheck;
	document.getElementById("btnZipClose").onclick = function(){
		window.close();
	}
}
function dongCheck(){
	if(zipForm.dongName.value == ""){
		alert("검색할 동 이름을 입력하세요");
		zipForm.dongName.focus();
		return false;
	}
	zipForm.submit();
}

function send(zipcode, area1, area2 ,area3, area4){
	opener.document.regForm.zipcode.value = zipcode;
	opener.document.regForm.address.value = area1 + " " + area2 + " " + area3 + " " + area4 + " ";
	window.close();
}
</script>
</head>
<body>
<br>
<form action="zipcheck.jsp" name="zipForm" method="post">
	<table class="table table-sm">
		<thead>
		<tr class="table-primary">
			<th colspan="4" >우편 번호 찾기</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>동 이름</td>
			<td><input type="text" name="dongName" style="width: 99%;"></td>
			<td><input type="button" value="검색" id="btnZipFind"></td>
			<td><input type="button" value="닫기" id="btnZipClose"><input type="hidden" name="check" value="n"></td>
		</tr>
		</tbody>
	</table>
</form>
<%
	if(check.equals("n")){
		if(list.isEmpty()){ //검색결과가 없을시
%>
	<b>검색 결과가 없습니다.</b>
<%
		}else{ //검색결과가 있을때
%>
	<table>
		<thead>
		<tr>
			<th>검색자료를 클릭하면 자동으로 주소가 입력됩니다</th>
		</tr>
		</thead>
		<tbody>
		<tr>
			<td>
			<%
				for(int i=0; i < list.size(); i++){
					ZipCodeDto dto = list.get(i);
					String zipcode = dto.getZipcode();
					String area1 = dto.getArea1();
					String area2 = dto.getArea2();
					String area3 = dto.getArea3();
					String area4 = dto.getArea4();
					if(area4 == null) area4 = "";
			%>
				<a href="javascript:send('<%=zipcode %>','<%=area1 %>','<%=area2 %>','<%=area3 %>','<%=area4 %>')" >
					<%=zipcode %> <%=area1 %> <%=area2 %> <%=area3 %> <%=area4 %>
				</a><br>
			<%
				}
			%>
			</td>
		</tr>
		</tbody>
	</table>
<%
		}
	}
%>
</body>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</html>