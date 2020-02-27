package pack1;

import java.io.FileInputStream;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;
import java.util.Properties;

public class DbTest2 {
	private Connection conn;
	private Statement stmt;
	private ResultSet rs;
	private Properties properties = new Properties();
	
	
	public DbTest2() { // Secure coding : 연결 정보를 별도 파일(userpass.properties)로 작성 후 읽기
		String sql = "";
		
		try {
			properties.load(new FileInputStream("C:\\work\\jsou\\javapro4_nomal\\src\\pack1\\userpass.properties")); //원래는 properties 파일 암호화 후 사용
//			System.out.println(properties.getProperty("driver")); // 값 읽어오기 확인
			Class.forName(properties.getProperty("driver"));
			conn = DriverManager.getConnection(properties.getProperty("url"),properties.getProperty("user"),properties.getProperty("passwd"));
			
			stmt = conn.createStatement();
			
			//자료 추가 -- auto commit 
			/******
			sql = "insert into sangdata values(5, '새우깡', 5, '1000')"; //문자나 날짜는 반드시 ' '로 둘러주기
			stmt.executeUpdate(sql);
			******/
			
			//transaction - 실제 작업은 이렇게 해야함
			/******
			conn.setAutoCommit(false);
			sql = "insert into sangdata values(6, '감자깡', 5, '1200')";
			stmt.executeUpdate(sql);
			// ... ... ... 
			//conn.rollback();
			conn.commit();
			conn.setAutoCommit(true);
			******/
			
			//자료 수정
			sql = "update sangdata set sang='꼬깔콘', dan=1300 where code=5	";
			int re = stmt.executeUpdate(sql); //return값 받기 - 실패시 0 
			if(re > 0) System.out.println("수정 성공");
			else		  System.out.println("수정 실패");
			
			
			//자료 삭제
			sql = "delete from sangdata where code=6";
			int re2 = stmt.executeUpdate(sql); //return값 받기 - 실패시 0 
			if(re2 > 0) System.out.println("삭제 성공");
			else		  System.out.println("삭제 실패");
			
			
			//모든 자료 읽기
			sql = "select * from sangdata order by code desc";
			int cou = 0;
			
			rs = stmt.executeQuery(sql);
			
			while(rs.next()) {
				System.out.println(rs.getString("code") + " " + rs.getString("sang") + " " + rs.getString("su") + " " + rs.getString("dan") + " ");
				cou++;
			}
			System.out.println("건수 : " + cou + "\n");
			
			
		} catch (Exception e) {
			System.out.println("에러 : " + e.getMessage());
		} finally {
			try {
				if(rs != null) rs.close();
				if(stmt != null) stmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("에러2 : " + e2.getMessage());
			}
		}
	}
	
	
	public static void main(String[] args) {
		new DbTest2();
	}
}
