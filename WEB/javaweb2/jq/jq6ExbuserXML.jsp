<?xml version="1.0" encoding="UTF-8"?>
<%@page import="java.sql.ResultSet"%>
<%@page import="java.sql.PreparedStatement"%>
<%@page import="java.sql.Connection"%>
<%@ page language="java" contentType="text/xml; charset=UTF-8"
	pageEncoding="UTF-8" import="java.sql.*"%>
<jikwons> 
<%
 	Connection conn = null;
 	PreparedStatement pstmt = null;
 	ResultSet rs = null;
 	String buser = request.getParameter("buser_name");
 	try {
 		Class.forName("org.mariadb.jdbc.Driver");
 	} catch (Exception e) {
 		e.printStackTrace();
 	}
 	try {

 		conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");

 		pstmt = conn.prepareStatement("SELECT distinct jikwon_no,jikwon_name,buser_tel,buser_name,(SELECT count(gogek_damsano) FROM jikwon b join gogek on jikwon_no = gogek_damsano  WHERE a.jikwon_no = b.jikwon_no) AS gogek_manage FROM jikwon a JOIN buser ON buser_no = buser_num left outer JOIN gogek ON jikwon_no = gogek_damsano WHERE buser_name = ?");
 	
 		pstmt.setString(1, buser);
 		rs = pstmt.executeQuery();
 		while (rs.next()) {
 %> 
	<jikwon> 
		<jikwon_no>
<%
 	out.print(rs.getString("jikwon_no"));
 %>
		</jikwon_no> 
		<jikwon_name> 
 <%
 	out.print(rs.getString("jikwon_name"));
 %> 
		</jikwon_name> 
		<buser_tel>
<%
 	out.print(rs.getString("buser_tel"));
 %> 
		</buser_tel> 
		<gogek_manage> 
<%
 	out.print(rs.getString("gogek_manage"));
 %>
		</gogek_manage> 
	</jikwon> 
<%
 	}
 		rs.close();
 		pstmt.close();
 		conn.close();
 	} catch (Exception e) {
 		e.printStackTrace();
 		return;
 	}
 %> 
 </jikwons>