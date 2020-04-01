<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr"></jsp:useBean>
<jsp:useBean id="dto" class="pack.board.BoardDto"></jsp:useBean>
<% 
	String num = request.getParameter("num"); 
	String spage = request.getParameter("page");
	
	dto = boardMgr.getData(num); //수정 대상 자료 읽기
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script type="text/javascript">
function check(){
	if(frm.pass.value === ""){
		alert("비밀번호 입력!");
		frm.pass.foucs();
		return;
	}
	
	if(confirm("정말 수정할까요?")){
		frm.submit();
	}
}
</script>
</head>
<body>
<form name="frm" method="post" action="editsave.jsp">
	<input type="hidden" name="num" value="<%=num%>">
	<input type="hidden" name="page" value="<%=spage%>">
	
	<table class="table table-bordered" style="width: 70%;">
		<tr>
			<td colspan="2" align="center" ><h2> 글쓰기 </h2></td>
		</tr>
		<tr>
			<td width="20%" align="center">이 름</td>
			<td><input name="name" style="width: 100%;" value="<%=dto.getName()%>"></td>
		</tr>
		<tr>
			<td align="center">암 호</td>
			<td><input type="password" name="pass" style="width: 100%;"></td>
		</tr>
		<tr>
			<td align="center">메 일</td>
			<td><input name="mail" style="width: 100%;" value="<%=dto.getMail()%>"></td>
		</tr>
		<tr>
			<td align="center">제 목</td>
			<td><input name="title" style="width: 100%;" value="<%=dto.getTitle()%>"></td>
		</tr>
		<tr>
			<td align="center">내 용</td>
			<td><textarea name="cont" rows="10" style="width: 100%;"><%=dto.getCont()%></textarea></td>
		</tr>
		<tr>
			<td align="center" colspan="2" height="30">
				<input type="button" value="수 정 완 료" onclick="check()">&nbsp;
				<input type="button" value="목  록" onclick="location.href='boardlist.jsp?page=<%=spage%>'">
			</td>
		</tr>
	</table>
</form>

<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>