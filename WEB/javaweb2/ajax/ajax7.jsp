<%@page import="java.util.ArrayList"%>
<%@ page language="java" contentType="text/plain; charset=UTF-8"
    pageEncoding="UTF-8"
	import = "java.sql.*"    
%>
<%
request.setCharacterEncoding("utf-8");

Connection conn = null;
PreparedStatement pstmt = null;
ResultSet rs = null;

String keyword = request.getParameter("keyword");

try{
	Class.forName("org.mariadb.jdbc.Driver");
}catch(Exception e){
	e.printStackTrace();
	return;
}

try{
	conn=DriverManager.getConnection("jdbc:mysql://192.168.0.66:3306/test", "root", "123");
	pstmt = conn.prepareStatement("select jikwon_name from jikwon where jikwon_name like ?");
	pstmt.setString(1, keyword + "%"); // para로 넘어온 값으로 >시작되는< 이름
	
	rs = pstmt.executeQuery();
	
	ArrayList<String> list = new ArrayList(); //데이터를 리스트에 담기
	
	while(rs.next()){
		list.add(rs.getString(1));
		//System.out.println(rs.getString(1));
	}
	
	out.print(list.size());
	out.print("|");
	for(int i = 0; i < list.size(); i++){
		String data = list.get(i);
		out.print(data);
		if(i < list.size() - 1){
			out.print(",");
		}
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