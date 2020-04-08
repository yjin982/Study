package aa.bb.Model;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Repository;

@Repository
public class DataDao {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	
//	@Qualifier("dataSource")
	@Autowired
	private MyDataSource dataSource;
	
	public DataDao() {}
	
	public ArrayList<SangpumDto> getDataAll(){
		ArrayList<SangpumDto> list = new ArrayList<SangpumDto>();
				
		try {
			String sql = "select * from sangdata";
			conn = dataSource.getConnection();
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
			
		}catch (Exception e) {
			System.out.println("getDataAll err " + e);
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();				
			}catch (Exception e2) {
				System.out.println("getDataAll close err" + e2);
			}
		}
		return list;
	}
}
