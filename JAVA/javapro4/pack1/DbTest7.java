package pack1;

import java.sql.Statement;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

public class DbTest7 {
	private Connection conn; // DB연결
	private PreparedStatement pstmt; // 선처리 방식으로 sql실행
	private ResultSet rs;  // select 결과에 접근
	
	
	public DbTest7() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");  // Maria DB 기준
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
		} catch (Exception e) {
			System.out.println("드라이버 로딩 실패 : " + e.getMessage());
		} 
		
		try {
			//자료 추가
			//statement처럼 처리할때
			//String insSql = "insert into sangdata values(6, 'aa', 5 ,100)";
			//pstmt = conn.prepareStatement(insSql);
			
			/*
			String insSql = "insert into sangdata values(?, ?, ?, ?)"; //값을 직접 입력하지 않기 때문에 보안성 o
			pstmt = conn.prepareStatement(insSql);
			pstmt.setString(1, "7");
			pstmt.setString(2, "아메리카노");
			pstmt.setInt(3, 10);
			pstmt.setInt(4, 5000);
			
			int re = pstmt.executeUpdate();
			if(re == 1) System.out.println("추가 성공"); //try catch 때문에 실행안됨
			else System.out.println("추가 실패");
			*/
			
			//자료 수정
			/*String upsql = "update sangdata set sang=?, su=? where code=?";
			pstmt = conn.prepareStatement(upsql);
			pstmt.setString(1, "삼다수");
			pstmt.setString(2, "100");
			pstmt.setString(3, "6");
			pstmt.executeUpdate();
			*/
			
			//자료 삭제
			/*String delsql = "delete from sangdata where code=?";
			pstmt = conn.prepareStatement(delsql);
			pstmt.setString(1, "7");
			pstmt.executeUpdate();
			*/
			
			//자료 보기
			String sql = "select code, sang, su, dan from sangdata";
			pstmt = conn.prepareStatement(sql); //sql문장을 처음에 한번만 컴파일
			
			rs = pstmt.executeQuery(); //
			while(rs.next()) {
				String code = rs.getString("code");
				String sangpum = rs.getString(2);
				int su = rs.getInt("su");
				String danga = rs.getString("dan");
				
				System.out.println(code + " " + sangpum + " " + su + " " + danga + " ");
			}
			
			sql = "select count(*) from sangdata";
			rs = pstmt.executeQuery(sql);
			if(rs.next()) {
				System.out.println("건수 : " + rs.getInt(1));
			}

		} catch (Exception e) {
			System.out.println("처리 실패 : " + e.getMessage());
		} finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				e2.printStackTrace();
			}
		}
	}
	
	public static void main(String[] args) {
		new DbTest7();
	}
}
