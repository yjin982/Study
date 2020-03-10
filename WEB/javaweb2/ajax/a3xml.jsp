<?xml version="1.0" encoding="UTF-8"?>
<%@ page language="java" contentType="text/xml; charset=UTF-8"
    pageEncoding="UTF-8"
	import="java.sql.*"    
%>

<sangpums>
<% 
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;

try{
	Class.forName("org.mariadb.jdbc.Driver");
}catch(Exception e){
	System.out.println("loading err : " + e);	
	return;
}


try{
	conn=DriverManager.getConnection("jdbc:mysql://192.168.0.66:3306/test","root","123");
	pstmt = conn.prepareStatement("select * from sangdata");
	rs = pstmt.executeQuery();
	
	while(rs.next()){
%>
	<sangpum>
		<code><%out.print(rs.getString("code")); %></code>
		<sang><%=rs.getString("sang") %></sang>
		<su><%=rs.getString("su") %></su>
		<dan><%=rs.getString("dan") %></dan>
	</sangpum>
<%
	}
}catch(Exception e){
	System.out.println("reading err : " + e);	
	return;
}finally{
	rs.close();
	pstmt.close();
	conn.close();
}
%>
</sangpums>