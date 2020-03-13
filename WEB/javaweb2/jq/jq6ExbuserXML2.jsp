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
 	String jikwon = request.getParameter("jikwon_name");
 	try {
 		Class.forName("org.mariadb.jdbc.Driver");
 	} catch (Exception e) {
 		e.printStackTrace();
 	}
 	try {

 		conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");

 		pstmt = conn.prepareStatement(
 				"SELECT gogek_name,gogek_tel,if(gogek_jumin LIKE '%-1%','남','여') as gender FROM jikwon join gogek on jikwon_no = gogek_damsano where jikwon_name = '"+jikwon+"'");
 		//pstmt.setString(1, jikwon);
 		rs = pstmt.executeQuery();
 		
 		while (rs.next()) {
 %> 
	<jikwon>
		<gogek_name> 
<%
 	out.print(rs.getString("gogek_name"));
 %> 
		</gogek_name> 
		<gogek_tel> 
<%
 	out.print(rs.getString("gogek_tel"));
 %> 
		</gogek_tel> 
		<gogek_jumin> 
<%
 	out.print(rs.getString("gender"));
 %> 
		</gogek_jumin> 
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