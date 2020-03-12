<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
    import="java.sql.*"%>
[    
<%
	request.setCharacterEncoding("utf-8");
	String jName = request.getParameter("jName");
	String jNo = request.getParameter("jNo");
	
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
		pstmt = conn.prepareStatement("select gogek_name, gogek_tel, if(substr(gogek_jumin,8,1)=1,'남','여') as gogek_gen " + 
					"from gogek inner join jikwon on gogek_damsano=jikwon_no " + 
					"where jikwon_name=? and jikwon_no= ?");
		pstmt.setString(1, jName);
		pstmt.setString(2, jNo);
		rs = pstmt.executeQuery();
		
		String result = "";
		while(rs.next()){
			result += "{";
			result += "\"name\":\"" + rs.getString("gogek_name") + "\",";
			result += "\"tel\":\"" + rs.getString("gogek_tel") + "\",";
			result += "\"gen\":\"" + rs.getString("gogek_gen") + "\"";
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