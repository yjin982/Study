<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
    import = "java.sql.*"
%>
[
<%
	Connection conn = null;
	PreparedStatement pstmt = null;
	ResultSet rs = null;
	
	//request.setCharacterEncoding("utf-8"); //한글 안 깨지게
	//String ss = request.getParameter("aaa"); //파라미터 받아오기

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
		
		Thread.sleep(5000); //비동기 시험
		
		String result = "";
		while(rs.next()){
			result += "{";
			result += "\"code\":\"" + rs.getString("code") + "\",";
			result += "\"sang\":\"" + rs.getString("sang") + "\",";
			result += "\"su\":\"" + rs.getString("su") + "\",";
			result += "\"dan\":\"" + rs.getString("dan") + "\"";
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