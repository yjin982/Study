package pack2;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class DbEx {
	private Connection conn = null;  			  // db와 연결할때 사용
	private PreparedStatement pstmt = null; // sql문 실행
	private ResultSet rs = null; 					  // 결과값 받아서 처리
	
	
	
	public DbEx() {
		try {
			Class.forName("org.mariadb.jdbc.Driver"); //마리아디비 드라이버 클래스를 읽어들임
			//jdbc:mariadb(프로토콜)://ip주소:마리아DB포트번호/디비이름  ////내컴퓨터 = localhost==127.0.0.1
			conn = DriverManager.getConnection("jdbc:mariadb://192.168.0.66:3306/test", "root", "123"); 
			pstmt = conn.prepareStatement("SELECT * FROM aa");
			rs = pstmt.executeQuery();
			
//			rs.next(); // 레코드 포인터를 다음으로 이동시킴, 자료가 있을경우 true, 없으면 false를 리턴
			while(rs.next()) {
				System.out.println(rs.getInt("bun") + " " + rs.getString("irum") + " " + rs.getString("juso"));
			}
			
		}catch (Exception e) {
			System.out.println("error : " + e.getMessage());
			
		}finally { //에러가 있든 없든 실행되는 구문
			try {
				rs.close();
				pstmt.close();
				conn.close();
				// 안한다고 에러가 떨어지는 것은 아니지만 권장사항
			}catch (Exception e) {
				System.out.println("error : " + e.getMessage());
			}
		}
	}
	
	
	public static void main(String[] args) {
		new DbEx();
	}
}
