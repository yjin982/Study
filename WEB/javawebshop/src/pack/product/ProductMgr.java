package pack.product;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.servlet.http.HttpServletRequest;
import javax.sql.DataSource;

import com.oreilly.servlet.MultipartRequest;
import com.oreilly.servlet.multipart.DefaultFileRenamePolicy;

import pack.order.OrderBean;

public class ProductMgr {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;
	
	public ProductMgr() {
		try {
			Context context = new InitialContext();
			ds = (DataSource)context.lookup("java:comp/env/jdbc_maria");		// java:comp/env/ ? 
		} catch (Exception e) {
			System.out.println("ProductMgr err : " + e);
		}
	}
	
	public ArrayList<ProductDto> getProductAll() { //전체 상품 가져오기
		ArrayList<ProductDto> list = new ArrayList<ProductDto>();
		
		try {
			String sql = "select * from shop_product order by no desc";
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				ProductDto dto = new ProductDto();
				dto.setNo(rs.getInt("no"));
				dto.setName(rs.getString("name"));
				dto.setPrice(rs.getString("price"));
				dto.setDetail(rs.getString("detail"));
				dto.setSdate(rs.getString("sdate"));
				dto.setStock(rs.getString("stock"));
				dto.setImage(rs.getString("image"));
				list.add(dto);
			}
			
		} catch (Exception e) {
			System.out.println("getProductAll err : " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("getProductAll close err : " + e2);
			}
		}
		
		return list;
	}
	
	public boolean insertProduct(HttpServletRequest request) { //상품 추가
		boolean b = false;
		
		try {
			// 업로드할 이미지 절대 경로
			String uploadDir = "C:\\work\\jsou\\javawebshop\\WebContent\\upload";
			
			MultipartRequest multi = new MultipartRequest(request, uploadDir, 5 * 1024 * 1024, "utf-8", new DefaultFileRenamePolicy());
			
			String sql = "insert into shop_product(name, price, detail, sdate, stock, image) values(?, ?, ?, now(), ?, ?)";
			// 날짜는 mariadb가 가진 날짜를 씀
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, multi.getParameter("name"));
			pstmt.setString(2, multi.getParameter("price"));
			pstmt.setString(3, multi.getParameter("detail"));
			pstmt.setString(4, multi.getParameter("stock"));
			
			if(multi.getFilesystemName("image") == null) {		// 이미지를 등록하지 않고 올리는 사람들을 위해 if문으로 구별 한다.
				pstmt.setString(5, "ready.gif");
			} else {
				pstmt.setString(5, multi.getFilesystemName("image"));
			}
			
			if(pstmt.executeUpdate() > 0) {				// insert 성공 시 true
				b = true;
			}
			
		} catch (Exception e) {
			System.out.println("insertProduct err : " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("insertProduct close err : " + e2);
			}
		}
		
		return b;
	}
	
	public ProductDto getProduct(String no) { //상품 정보 얻기
		ProductDto dto = null;
		String sql = "select * from shop_product where no = ?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, no);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				dto = new ProductDto();
				dto.setNo(rs.getInt("no"));
				dto.setName(rs.getString("name"));
				dto.setPrice(rs.getString("price"));
				dto.setDetail(rs.getString("detail"));
				dto.setSdate(rs.getString("sdate"));
				dto.setStock(rs.getString("stock"));
				dto.setImage(rs.getString("image"));
			}
			
		} catch (Exception e) {
			System.out.println("getProduct err : " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("getProduct close err : " + e2);
			}
		}
		return dto;
	}
	
	public boolean updateProduct(HttpServletRequest request) {//상품 수정하기
		boolean b = false;
		
		try {
			// 업로드할 이미지 절대 경로
			String uploadDir = "C:\\work\\jsou\\javawebshop\\WebContent\\upload";
			MultipartRequest multi = new MultipartRequest(request, uploadDir, 5 * 1024 * 1024, "utf-8", new DefaultFileRenamePolicy());
						
			conn = ds.getConnection();
			if(multi.getFilesystemName("image") == null) {
				String sql = "update shop_product set name=?, price=?, detail=?, stock=? where no=?";
				pstmt = conn.prepareStatement(sql);
				
				pstmt.setString(1, multi.getParameter("name"));
				pstmt.setString(2, multi.getParameter("price"));
				pstmt.setString(3, multi.getParameter("detail"));
				pstmt.setString(4, multi.getParameter("stock"));
				pstmt.setString(5, multi.getParameter("no"));
				
			}else {
				String sql = "update shop_product set name=?, price=?, detail=?, stock=?, image=? where no=?";
				pstmt = conn.prepareStatement(sql);
				
				pstmt.setString(1, multi.getParameter("name"));
				pstmt.setString(2, multi.getParameter("price"));
				pstmt.setString(3, multi.getParameter("detail"));
				pstmt.setString(4, multi.getParameter("stock"));
				pstmt.setString(5, multi.getFilesystemName("image"));
				pstmt.setString(6, multi.getParameter("no"));
			}
			
			if(pstmt.executeUpdate() > 0) b = true;

		}catch (Exception e) {
			System.out.println("updateProduct err : " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("updateProduct close err : " + e2);
			}
		}
		
		return b;
	}
	
	public boolean deleteProduct(String no) { //상품 삭제하기
		boolean b = false;
		String sql = "delete from shop_product where no=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, no);
			
			if(pstmt.executeUpdate() > 0) b = true;
			
		}catch (Exception e) {
			System.out.println("deleteProduct err : " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("deleteProduct close err : " + e2);
			}
		}
		return b;
	}

	public void reduceProduct(OrderBean orderBean) { //고객이 상품 주문 결제시 주문 수량 만큼 재고량에서 빼기
		String sql = "update shop_product set stock=(stock-?) where no=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, orderBean.getQuantity());
			pstmt.setString(2, orderBean.getProduct_no());
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("reduceProduct err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("reduceProduct close err " + e2);
			}
		}
	}
	
}
