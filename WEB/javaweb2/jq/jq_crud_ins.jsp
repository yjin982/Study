<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
	import="java.sql.*"%>

<% 
	request.setCharacterEncoding("utf-8");
	String code = request.getParameter("code");
	String sang = request.getParameter("sang");
	String su = request.getParameter("su");
	String dan = request.getParameter("dan");
	
	//System.out.println(code+sang+su+dan);

	Connection conn = null;
	PreparedStatement pstmt = null;
	
	
	try{
		Class.forName("org.mariadb.jdbc.Driver");
		conn=DriverManager.getConnection("jdbc:mysql://192.168.0.66:3306/test","root","123");
		pstmt = conn.prepareStatement("insert into sangdata values(?, ?, ?, ?)");
		pstmt.setInt(1, Integer.parseInt(code));
		pstmt.setString(2, sang);
		pstmt.setInt(3, Integer.parseInt(su));
		pstmt.setInt(4, Integer.parseInt(dan));
		
		int re = pstmt.executeUpdate();
		System.out.println(re);
		if(re == 0)
			out.print("false");
		else
			out.print("true");
		
	}catch(Exception e){
		//e.printStackTrace();
		return;
	}finally{
		pstmt.close();
		conn.close();
	}
%>