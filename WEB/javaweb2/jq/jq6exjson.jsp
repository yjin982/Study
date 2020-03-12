<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
    import="java.sql.*"%>
[    
<%
	request.setCharacterEncoding("utf-8");
	String bName = request.getParameter("bName");
	
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
		pstmt = conn.prepareStatement("select jikwon_no, jikwon_name, buser_tel, count(gogek_no) as gogeksu " + 
					"from jikwon inner join buser on buser_num=buser_no left outer join gogek on gogek_damsano=jikwon_no " + 
					"where buser_name=? group by jikwon_no");
		pstmt.setString(1, bName);
		rs = pstmt.executeQuery();
		
	
		String result = "";
		while(rs.next()){
			result += "{";
			result += "\"no\":\"" + rs.getString("jikwon_no") + "\",";
			result += "\"name\":\"" + rs.getString("jikwon_name") + "\",";
			result += "\"buserTel\":\"" + rs.getString("buser_tel") + "\",";
			result += "\"gogeksu\":\"" + rs.getString("gogeksu") + "\"";
			result += "},";
		}
		if(result.length() > 0){
			result = result.substring(0, result.length()-1);
		}
		out.print(result);
	}catch(Exception e){
		e.printStackTrace();
		return;
	}finally{
		rs.close();
		pstmt.close();
		conn.close();
	}


%>
]