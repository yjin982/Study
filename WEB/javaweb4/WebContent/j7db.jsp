<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" import="java.sql.*" %>
<%
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;
	
	try{
		Class.forName("org.mariadb.jdbc.Driver");
		conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/test", "root", "123");
		pstmt = conn.prepareStatement("select * from sangdata");
		
	}catch(Exception e){
		out.println("연결 에러" + e);
		e.printStackTrace();
		return;
	}
%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<h2>* 상품자료(jsp:Beans X)</h2>
<table border="1" style="border-collapse: collapse;">
	<tr>
		<th>code</th><th>sang</th><th>su</th><th>dan</th>
	</tr>
<%
	try{
		rs = pstmt.executeQuery();
		while(rs.next()){
%>
		<tr>
			<td><%=rs.getString("code")%></td>
			<td><%=rs.getString("sang")%></td>
			<td><%=rs.getString("su")%></td>
			<td><%=rs.getString("dan")%></td>
		</tr>
<%	
		}
	}catch(Exception e){
		out.println("실행 에러" + e);
	}finally{
		rs.close();
		pstmt.close();
		conn.close();
	}
%>
</table>
</body>
</html>