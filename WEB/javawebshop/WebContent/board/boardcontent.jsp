<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr"></jsp:useBean>
<jsp:useBean id="dto" class="pack.board.BoardDto"></jsp:useBean>
<%
	String num = request.getParameter("num");
	String spage = request.getParameter("page");
	
	boardMgr.updateReadcnt(num);
	dto = boardMgr.getData(num);
	
	String name = dto.getName();
	String pass = dto.getPass();
	String mail = dto.getMail();
	String bdate = dto.getBdate();
	int cnt = dto.getReadcnt();
	String title = dto.getTitle();
	String cont = dto.getCont();
	String bip = dto.getBip();
	
	String apass = "***"; //어드민일때만 비밀번호가 보이게
	String adminOk = (String)session.getAttribute("adminOk");
	if(adminOk != null){
		if(adminOk.equals("admin")) apass = pass;
	}
%>
    
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
</head>
<body>
<h2> </h2>
<table class="table table-bordered" style="width: 70%;">
	<tr>
		<td><b>비밀번호 : <%=apass%></b></td>
		<td colspan="2" style="text-align: right;">
			<a href="reply.jsp?num=<%=num%>&page=<%=spage%>">
				<img src="../images/reply.gif" />
			</a>
			<a href="edit.jsp?num=<%=num%>&page=<%=spage%>">
				<img src="../images/edit.gif" />
			</a>
			<a href="delete.jsp?num=<%=num%>&page=<%=spage%>">
				<img src="../images/del.gif" />
			</a>
			<a href="boardlist.jsp?page=<%=spage%>">
				<img src="../images/list.gif" />
			</a>
		</td>
	</tr>
	<tr>
		<td>작성자 : <a href="mailto:<%=mail%>"><%=name %></a> (ip : <%=bip %>)</td>
		<td>작성일 : <%=bdate %></td>
		<td>조회수 : <%=cnt %></td>
	</tr>
	<tr>
		<td colspan="3">제목 : <%=title %></td>
	</tr>
	<tr>
		<td colspan="3">
			<textarea rows="10" readonly="readonly" style="width: 100%;"><%=cont %></textarea>
		</td>
	</tr>
</table>


<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>