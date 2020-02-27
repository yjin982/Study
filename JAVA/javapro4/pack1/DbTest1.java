package pack1;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DbTest1 {
	private Connection conn; // DB연결
	private Statement stmt; // SQL 실행
	private ResultSet rs;  // select 결과에 접근
	
	
	public DbTest1() {
		// Driver loading 방법 1) 드라이버 파일을 구해서 프로젝트에 build path 에 추가
		try {
			Class.forName("org.mariadb.jdbc.Driver");  // Maria DB 기준
		} catch (Exception e) {
			System.out.println("드라이버 로딩 실패 : " + e.getMessage());
		} 
		
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
		} catch (Exception e) {
			System.out.println("연결 실패 : " + e.getMessage());
		} 
		
		try {
			stmt = conn.createStatement();
			/*
			rs = stmt.executeQuery("select * from sangdata"); //비권장사항
			rs.next();
			System.out.println(rs.getString("code") + " " + rs.getString("sang") + " " + rs.getString("su") + " " + rs.getString("dan") + " ");
			*/
			
			/*
			rs = stmt.executeQuery("select code as 코드, sang as 품명, su as 수량,  dan as 단가 from sangdata");
			rs.next();
			System.out.println(rs.getString("코드") + " " + rs.getString("sang") + " " + rs.getInt(3)+ " " + rs.getString("dan") + " ");
			*/
			
			rs = stmt.executeQuery("select code, sang, su, dan from sangdata"); //권장사항 *보다 좀 더 빠름
			while(rs.next()) {
				String code = rs.getString("code");
				String sangpum = rs.getString(2);
				int su = rs.getInt("su");
				String danga = rs.getString("dan");
				
				System.out.println(code + " " + sangpum + " " + su + " " + danga + " ");
			}
			
			String sql = "select count(*) from sangdata";
			rs = stmt.executeQuery(sql);
			if(rs.next()) {
				System.out.println("건수 : " + rs.getInt(1));
			}

		} catch (Exception e) {
			System.out.println("처리 실패 : " + e.getMessage());
		} finally {
			try {
				if(rs != null) rs.close();
				if(stmt != null) stmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
	}
	
	public static void main(String[] args) {
		new DbTest1();
	}
}
