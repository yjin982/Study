package pack.order;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class OrderMgr {
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;
	
	public OrderMgr() {
		try {
			Context context = new InitialContext();
			ds = (DataSource)context.lookup("java:comp/env/jdbc_maria");	
		} catch (Exception e) {
			System.out.println("OrderMgr err : " + e);
		}
	}
	
	public void insertOrder(OrderBean orderBean) { //카트에 담긴 상품을 order 테이블로 넣기(=주문하기)
		String sql = "insert into shop_order(product_no, quantity, sdate, state, id) values(?, ?, now(), ?, ?)";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, orderBean.getProduct_no());
			pstmt.setString(2, orderBean.getQuantity());
			pstmt.setString(3, "1"); //state는 주문 상태: 없으면 접수중, 1은 접수완료, 2은 입금확인, 3은 배송준비, 4는 배송중, 5는 처리완료 (각자 원하는대로)
			pstmt.setString(4, orderBean.getId());
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("insertOrder err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("insertOrder close err " + e2);
			}
		}
	}
	
	public ArrayList<OrderDto> getOrder(String id){ //로그인한 고객만의 주문 목록 보여주기
		ArrayList<OrderDto> list = new ArrayList<OrderDto>();
		String sql = "select * from shop_order where id=? order by no desc";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, id);
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				OrderDto dto = new OrderDto();
				dto.setNo(rs.getString("no"));
				dto.setProduct_no(rs.getString("product_no"));
				dto.setQuantity(rs.getString("quantity"));
				dto.setSdate(rs.getString("sdate"));
				dto.setState(rs.getString("state"));
				dto.setId(rs.getString("id"));
				list.add(dto);
			}
			
		}catch (Exception e) {
			System.out.println("getOrder err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("getOrder close err " + e2);
			}
		}
		return list;
	}
	
	public ArrayList<OrderDto> getOrderAll(){ //주문 목록 전체 보기
		ArrayList<OrderDto> list = new ArrayList<OrderDto>();
		String sql = "select * from shop_order order by no desc";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			
			while(rs.next()) {
				OrderDto dto = new OrderDto();
				dto.setNo(rs.getString("no"));
				dto.setProduct_no(rs.getString("product_no"));
				dto.setQuantity(rs.getString("quantity"));
				dto.setSdate(rs.getString("sdate"));
				dto.setState(rs.getString("state"));
				dto.setId(rs.getString("id"));
				list.add(dto);
			}
			
		}catch (Exception e) {
			System.out.println("getOrderAll err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("getOrderAll close err " + e2);
			}
		}
		return list;
	}
	
	public OrderDto getOrderDetail(String no) { //주문한 상품의 각 상세 정보 보기
		OrderDto dto = null;
		String sql = "select * from shop_order where no=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, no);
			rs = pstmt.executeQuery();
			while(rs.next()) {
				dto = new OrderDto();
				dto.setNo(no);
				dto.setId(rs.getString("id"));
				dto.setProduct_no(rs.getString("product_no"));
				dto.setQuantity(rs.getString("quantity"));
				dto.setSdate(rs.getString("sdate"));
				dto.setState(rs.getString("state"));
			}
			
		}catch (Exception e) {
			System.out.println("getOrderDetail err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("getOrderDetail close err " + e2);
			}
		}
		return dto;
	}
	
	public boolean updateOrder(String no, String state) { //관리자 주문 상태 변경
		boolean b = false;
		String sql = "update shop_order set state=? where no=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, state);
			pstmt.setString(2, no);
			
			if(pstmt.executeUpdate() > 0) b = true;
			
		}catch (Exception e) {
			System.out.println("updateOrder err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("updateOrder close err " + e2);
			}
		}
		return b;
	}
	
	public boolean deleteOrder(String no) { //관리자 주문 삭제
		boolean b = false;
		String sql = "delete from shop_order where no=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, no);
			
			if(pstmt.executeUpdate() > 0) b = true;
			
		}catch (Exception e) {
			System.out.println("deleteOrder err " + e);
		} finally {
			try {
				if(rs != null) { rs.close(); }
				if(pstmt != null) { pstmt.close(); }
				if(conn != null) { conn.close(); }
			} catch (Exception e2) {
				System.out.println("deleteOrder close err " + e2);
			}
		}
		return b;
	}
	
	
}
