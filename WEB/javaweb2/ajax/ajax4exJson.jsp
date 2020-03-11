<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
    import = "java.sql.*"
%>
{"jikwon":
	[
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

	try{
		Class.forName("org.mariadb.jdbc.Driver");
	}catch(Exception e){
		System.out.println("loading err : " + e);	
		return;
	}
	
	try{
		conn=DriverManager.getConnection("jdbc:mysql://192.168.0.66:3306/test","root","123");
		pstmt = conn.prepareStatement(sql);
		rs = pstmt.executeQuery();
		
		String result = "";
		while(rs.next()){
			result += "{";
			result += "\"no\":\"" + rs.getString("jikwon_no") + "\",";
			result += "\"name\":\"" + rs.getString("jikwon_name") + "\",";
			result += "\"jik\":\"" + rs.getString("jikwon_jik") + "\",";
			result += "\"gen\":\"" + rs.getString("jikwon_gen") + "\"";
			result += "},";
		}
		if(result.length() > 0){
			result = result.substring(0, result.length()-1);
		}
		out.println(result);
	}catch(Exception e){
		e.printStackTrace();
		//System.out.println("reading err : " + e);	
		return;
	}finally{
		rs.close();
		pstmt.close();
		conn.close();
	}
	%>
	]
}