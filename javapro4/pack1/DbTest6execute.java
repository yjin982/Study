package pack1;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

public class DbTest6execute {
	Connection conn;
	Statement stmt;
	ResultSet rs;
	
	
	public DbTest6execute() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");  // Maria DB 기준
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			
			process();
			
		} catch (Exception e) {
			System.out.println("연결 실패 : " + e.getMessage());
			
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
	
	private void process() {
		try {
			stmt = conn.createStatement();
			
			boolean b = false;
			b = stmt.execute("update sangdata set sang='종이컵' where code=5");
			System.out.println("sangdata update 수행 후 b : " + b); //false 반환, 업데이트는 성공
			int re = stmt.getUpdateCount(); // insert, update, delete 수행 후 결과 수를 반환
			
			if(re >= 1) {
				System.out.println("작업 성공");
			}else {
				System.out.println("작업 실패");
			}
			
			b = stmt.execute("select * from sangdata");
			System.out.println("sangdata select 수행 후 b : " + b); //true 반환, select 이외에는 false로
			/*b = stmt.execute("select * from def");
			System.out.println("def(빈테이블) select 수행 후 b : " + b);*/
			
			//b로 select 인지를 확인하고 rs를 받음
			if(b) {
				rs = stmt.getResultSet();
				while(rs.next()) {
					System.out.println(rs.getString(1) + " " + rs.getString(2));
				}
			}
			
			
		}catch (Exception e) {
			System.out.println("process 실패 : " + e.getMessage());
		}
	}
	
	
	
	public static void main(String[] args) {
		new DbTest6execute();
	}
}
