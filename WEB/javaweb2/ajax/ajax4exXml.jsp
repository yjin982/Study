<?xml version="1.0" encoding="UTF-8"?>
<%@ page language="java" contentType="text/xml; charset=UTF-8"
    pageEncoding="UTF-8"
    import="java.sql.*"
%>
<jikwons>
<% 
String gen = request.getParameter("gen");
String sql = "select jikwon_no, jikwon_name, jikwon_jik, jikwon_gen from jikwon";
Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;

if(gen.equals("m")){
	sql += " where jikwon_gen='남'";
}else if(gen.equals("f")){
	sql += " where jikwon_gen='여'";
}
out.print(sql);
try{
	Class.forName("org.mariadb.jdbc.Driver");
}catch(Exception e){
	e.printStackTrace();
	return;
}

try{
	conn=DriverManager.getConnection("jdbc:mysql://192.168.0.66:3306/test","root","123");
	pstmt = conn.prepareStatement(sql);
	rs = pstmt.executeQuery();
	
	while(rs.next()){
%>
	<jikwon>
		<no><%=rs.getString("jikwon_no") %></no>
		<name><%=rs.getString("jikwon_name") %></name>
		<jik><%=rs.getString("jikwon_jik") %></jik>
		<gen><%=rs.getString("jikwon_gen") %></gen>
	</jikwon>
<% 
	}
}catch(Exception e){
	e.printStackTrace();
	return;
}finally{
	rs.close();
	pstmt.close();
	conn.close();
}
%>
</jikwons>