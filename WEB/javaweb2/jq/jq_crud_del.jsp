<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
	import="java.sql.*"%>

<% 
	request.setCharacterEncoding("utf-8");
	String dcode = request.getParameter("dcode");

	Connection conn = null;
	PreparedStatement pstmt = null;
	
	
	try{
		Class.forName("org.mariadb.jdbc.Driver");
		conn=DriverManager.getConnection("jdbc:mysql://192.168.0.66:3306/test","root","123");
		pstmt = conn.prepareStatement("delete from sangdata where code=?");
		pstmt.setInt(1, Integer.parseInt(dcode));

		int re = pstmt.executeUpdate();
		
		if(re > 0)
			out.print("true");
		else
			out.print("false");
		
	}catch(Exception e){
		e.printStackTrace();
		return;
	}finally{
		pstmt.close();
		conn.close();
	}
%>