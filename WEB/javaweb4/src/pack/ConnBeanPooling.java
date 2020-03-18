package pack;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class ConnBeanPooling {
	private Connection conn; //conn 하나만 쓰는 걸 개선 => JDBC Connection pooling
	private PreparedStatement pstmt;
	private ResultSet rs;
	private  DataSource ds;
	
	public ConnBeanPooling() { //context에서 드라이브 로딩하기 Class.forName로 로딩할 필요없음
		try {
			Context context = new InitialContext(); //dbcp 지원
			ds = (DataSource)context.lookup("java:comp/env/jdbc_maria"); //오브젝트로 넘어오기때문에 캐스팅
		} catch (Exception e) {
			System.out.println("DB connection");
			e.printStackTrace();
		}
	}
	
	public ArrayList<SangpumDto> getDataAll(){
		ArrayList<SangpumDto> list = new ArrayList<SangpumDto>();
		
		try {
			conn = ds.getConnection(); 
			String sql = "select * from sangdata";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				SangpumDto dto = new SangpumDto();
				dto.setCode(rs.getString("code"));
				dto.setSang(rs.getString("sang"));
				dto.setSu(rs.getString("su"));
				dto.setDan(rs.getString("dan"));
				list.add(dto);
			}
		} catch (Exception e) {
			System.out.println("getDataAll");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("close");
				e2.printStackTrace();
			}
		}
		return list;
	}
	
	public boolean insertData(SangpumBean bean) {
		boolean b = false;
		
		try {
			//새상품 code 구하기
			String sql = "select max(code) as max from sangdata";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();

			int newCode = 0;
			if(rs.next()) newCode = rs.getInt("max")+1;
			else newCode++;
//			System.out.print(newCode);
			pstmt.close();
			
			//insert
			sql = "insert into sangdata values(?,?,?,?)";
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, newCode);
			pstmt.setString(2, bean.getSang());
			pstmt.setString(3, bean.getSu());
			pstmt.setString(4, bean.getDan());
			if(pstmt.executeUpdate() == 1) b = true;

		} catch (Exception e) {
			System.out.println("insertData");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("close");
				e2.printStackTrace();
			}
		}
		return b;
	}
	
	public SangpumDto updateList(String code) {
		SangpumDto dto = null;
		
		try {
			//수정할 데이터 불러오기
			String sql = "select * from sangdata where code=?";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, code);
			rs = pstmt.executeQuery();

			if(rs.next()) {
				dto = new SangpumDto();
				dto.setCode(code);
				dto.setSang(rs.getString("sang"));
				dto.setSu(rs.getString("su"));
				dto.setDan(rs.getString("dan"));
			}
			
		} catch (Exception e) {
			System.out.println("updateList");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("close");
				e2.printStackTrace();
			}
		}
		return dto;
	}
	
	public boolean updateData(SangpumBean bean) {
		boolean b = false;
		
		try {
			//수정할 데이터 불러오기
			String sql = "update sangdata set sang=?,su=?,dan=? where code=?";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, bean.getSang());
			pstmt.setString(2, bean.getSu());
			pstmt.setString(3, bean.getDan());
			pstmt.setString(4, bean.getCode());
			if(pstmt.executeUpdate() > 0) b = true;

		} catch (Exception e) {
			System.out.println("updateData");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("close");
				e2.printStackTrace();
			}
		}
		
		return b;
	}
	
	public boolean deleteData(String code) {
		boolean b = false;
		
		try {
			String sql ="delete from sangdata where code=?";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, code);
			
			if(pstmt.executeUpdate() > 0) b = true;
			
		} catch (Exception e) {
			System.out.println("deleteData");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("close");
				e2.printStackTrace();
			}
		}
		
		return b;
	}
}
