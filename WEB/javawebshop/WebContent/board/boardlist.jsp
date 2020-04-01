<%@page import="pack.board.BoardMgr" %>
<%@page import="pack.board.BoardDto" %>
<%@page import="java.util.ArrayList" %>
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
    
<jsp:useBean id="boardMgr" class="pack.board.BoardMgr"></jsp:useBean>
<jsp:useBean id="dto" class="pack.board.BoardDto"></jsp:useBean>
<%  
	request.setCharacterEncoding("utf-8");
	int pageSu, spage = 1; //페이지 나누기 위한 변수
%>

<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>게시판</title>
<link rel="stylesheet" type="text/css" href="../css/board.css">
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css" integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" crossorigin="anonymous">
<script type="text/javascript">
window.onload = function(){
	document.getElementById("btnSearch").onclick = function(){
		if(frm.sword.value == ""){ //검색어가 없을 경우
			frm.sword.focus();
			alert("검색어를 입력하시오");
			return false;
		}
		frm.submit();
	}
}
</script>
</head>
<body>
<h1>&nbsp;</h1>
<table>
	<tr>
		<td>
			<div align="center">
			[<a href="../index.jsp">메인으로</a>]&nbsp;
			[<a href="boardlist.jsp?page=1">최근목록</a>]&nbsp;
			[<a href="boardwrite.jsp">새글작성</a>]&nbsp;
			[<a href="#" onclick="window.open('admin.jsp','','width=400,height=150,top=200,left=300')">관리자용</a>]&nbsp;
			</div>
			<br/><br/>
			<table class="table table-bordered table-hover">
				<thead class="thead-dark">
				<tr>
					<th scope="col">번호</th><th scope="col">글 제목</th><th scope="col">작성자</th><th scope="col">작성일</th><th scope="col">조회</th>
				</tr>
				</thead>
				<%
					//paging 처리
					try{
						spage = Integer.parseInt(request.getParameter("page")); //현재 페이지 값
					}catch(Exception e){
						spage = 1;
					}
					if(spage <= 0) spage = 1;   //out.print("spage : " + spage);
					
					boardMgr.totalList(); //전체 레코드 수 구하기
					pageSu = boardMgr.getPageSu(); //전체 페이지 수 구하기
					///////////
					
					//검색 처리 : 검색따로 처리하는게 좋지만 한꺼번에 하는걸로
					//ArrayList<BoardDto> list = boardMgr.getDataAll(spage); //다 가져오지 말고 5개씩 가져오도록 매개변수 넣은걸로 변경
					//한글 처리 여기서 하면 안 먹음
					String stype = request.getParameter("stype");
					String sword = request.getParameter("sword");
					
					ArrayList<BoardDto> list = boardMgr.getDataAll(spage, stype, sword);
					for(int i = 0; i < list.size(); i++){
						dto = list.get(i);
						//댓글 들여쓰기 처리
						int nst = dto.getNested();
						String tab = "";
						for(int j = 0; j < nst; j++){
							tab += "&nbsp;&nbsp;";
						}
						//////////
				%>
				<tr>
					<th scope="row"><%=dto.getNum() %></td>
					<td>
						<%=tab %><a href="boardcontent.jsp?num=<%=dto.getNum() %>&page=<%=spage%>"><%=dto.getTitle() %></a>
					</td>
					<td><%=dto.getName() %></td>
					<td><%=dto.getBdate() %></td>
					<td><%=dto.getReadcnt() %></td>
				</tr>
				<%			
					}
				%>
			</table><br/>
			<table style="width: 100%;">
				<tr>
					<td style="text-align: center;">
						<%
							for(int i = 1; i <= pageSu; i++){
								if(i == spage){
									out.print("<b> [" + i + "] </b>");
								}else{
									out.print("<a href='boardlist.jsp?page=" + i + "'> [" + i + "] </a>");
								}
							}
						%><br><br>
						<form action="boardlist.jsp" name="frm" method="post">
							<select name="stype">
								<option value="title" selected="selected">글제목</option>
								<option value="name">작성자</option>			
							</select>
							<input type="text" name="sword">							
							<input type="button" value="검색" id="btnSearch">
						</form>
					</td>
				</tr>
			</table>
		</td>
	</tr>
</table>


<script src="https://code.jquery.com/jquery-3.4.1.slim.min.js" integrity="sha384-J6qa4849blE2+poT4WnyKhv5vZF5SrPo0iEjwBvKU7imGFAV0wwj1yYfoRSJoZ+n" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
</body>
</html>