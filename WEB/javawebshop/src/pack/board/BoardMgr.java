package pack.board;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;

import javax.naming.Context;
import javax.naming.InitialContext;
import javax.sql.DataSource;

public class BoardMgr { //게시판 비즈니스 로직
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;
	private DataSource ds;
	
	private int tot; //페이징 처리 : 전체 레코드수
	private int pList = 5; //페이지당 출력 행 수
	private int pageSu; //전체 페이지 수
	
	public BoardMgr() { //생성자를 통해 dbcp처리
		try { 
			Context context = new InitialContext();
			ds = (DataSource)context.lookup("java:comp/env/jdbc_maria");
		} catch (Exception e) {
			System.out.println("board manager err");
			e.printStackTrace();
		}
	}
	
	public int currentGetNum() { //가장 최근 글 숫자 구하기
		String sql = "select max(num) as max from shopboard";
		int cnt = 0;

		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			if(rs.next()) cnt = rs.getInt(1);		
			
		}catch (Exception e) {
			System.out.println("currentGetNum err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("currentGetNum close err");
				e.printStackTrace();
			}
		}
		return (cnt + 1);
	}
	
	public void saveData(BoardBean bean) { //글 작성(=레코드 저장)
		String sql = "insert into shopboard values(?,?,?,?,?,?,?,?,?,?,?,?)";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, bean.getNum());
			pstmt.setString(2, bean.getName());
			pstmt.setString(3, bean.getPass());
			pstmt.setString(4, bean.getMail());
			pstmt.setString(5, bean.getTitle());
			pstmt.setString(6, bean.getCont());
			pstmt.setString(7, bean.getBip());
			pstmt.setString(8, bean.getBdate());
			pstmt.setInt(9, 0); //readcnt 조회수, 작성이니까
			pstmt.setInt(10, bean.getGnum()); 
			pstmt.setInt(11, 0); //onum 원글이니까
			pstmt.setInt(12, 0); //nested ,,
			
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("savaData err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("savaData close err");
				e.printStackTrace();
			}
		}
	}
	
	public ArrayList<BoardDto> getDataAll(int page, String stype, String sword){ //전체 글(=레코드) 가져오기
		ArrayList<BoardDto> list = new ArrayList<BoardDto>();
		
//		String sql = "select * from shopboard order by gnum desc, onum asc";
		String sql = "select * from shopboard";
		try {
			conn = ds.getConnection();
			
			if(sword == null) { //검색이 아닐 경우
				sql += " order by gnum desc, onum asc";
				pstmt = conn.prepareStatement(sql);
			}else { //검색
				sql += " where " + stype + " like ?";
				sql += " order by gnum desc, onum asc";
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, "%" + sword + "%");
			}
			
			rs = pstmt.executeQuery();
			
			for (int i = 0; i < (page - 1) * pList; i++) { //page 값이 3일 경우 2*5 = 9번째 레코드로 포인터가 이동
				rs.next(); //레코드 포인터 위치 이동
			}
			
			int k = 0;
			while(rs.next() && k < pList) { //레코드 이동 후 그 다음에 있는 레코드(10부터) 5개만 가져옴
				BoardDto dto = new BoardDto();
				dto.setNum(rs.getInt(1));
				dto.setTitle(rs.getString("title"));
				dto.setName(rs.getString("name"));
				dto.setBdate(rs.getString("bdate"));
				dto.setReadcnt(rs.getInt("readcnt"));
				dto.setNested(rs.getInt("nested"));
				list.add(dto);
				k++;
			}
		}catch (Exception e) {
			System.out.println("getDataAll err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("getDataAll close err");
				e.printStackTrace();
			}
		}
		return list; 
	}
	
	public void totalList() { //전체 레코드 수 가져오기 => 페이징
		String sql = "select count(*) from shopboard";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			rs.next();
			tot = rs.getInt(1);  //전체 건수(멤버필드로 만들어둔 변수에 저장)
			
		}catch (Exception e) {
			System.out.println("totalList err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("totalList close err");
				e.printStackTrace();
			}
		}
	}
	
	public int getPageSu() { //총 페이지 수 반환 => 페이징
		pageSu = tot / pList;
		/** 남은 글 페이징 처리 : 만약 글이 21개 일때 pageSu가 4가 되어버리는데 남은 글 1개도 페이징에 들어가도록 +1*/
		if(tot % pList > 0) pageSu++;
		
		return pageSu;
	}
	
	public void updateReadcnt(String num) { //글 내용 보기 전에 조회수 증가
		String sql = "update shopboard set readcnt=readcnt+1 where num=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("updateReadcnt err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("updateReadcnt close err");
				e.printStackTrace();
			}
		}
	}
	
	public BoardDto getData(String num) { //게시글 상세 보기
		String sql = "select * from shopboard where num=?";
		BoardDto dto = null;
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				dto = new BoardDto();
				dto.setName(rs.getString("name"));
				dto.setPass(rs.getString("pass"));
				dto.setMail(rs.getString("mail"));
				dto.setTitle(rs.getString("title"));
				dto.setCont(rs.getString("cont"));
				dto.setBip(rs.getString("bip"));
				dto.setBdate(rs.getString("bdate"));
				dto.setReadcnt(rs.getInt("readcnt"));
			}
		} catch (Exception e) {
			System.out.println("getData err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("getData close err");
				e.printStackTrace();
			}
		}
		return dto;
	}
	
	public BoardDto getReplyData(String num) { //답글쓰기= 원글내용 가져오기
		String sql = "select * from shopboard where num=?";
		BoardDto dto = null;
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				dto = new BoardDto();
				dto.setTitle(rs.getString("title"));
				dto.setGnum(rs.getInt("gnum"));
				dto.setOnum(rs.getInt("onum"));
				dto.setNested(rs.getInt("nested"));
				
			}
		} catch (Exception e) {
			System.out.println("getData err");
			e.printStackTrace();
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("getData close err");
				e.printStackTrace();
			}
		}
		return dto;
	}
	
	public void updateOnum(int gnum, int onum) { //댓글 onum 갱신
		String sql = "update shopboard set onum=onum+1 where onum >= ? and gnum = ?";
		/* 같은 그룹의 레코드는 모두 작업에 참여
		 * 댓글의 onum은 이미 db에 있는 onum 보다 크거나 같은 값으로 변경
		 * */
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, onum);
			pstmt.setInt(2, gnum);
			pstmt.executeUpdate();
			
		} catch (Exception e) {
			System.out.println("updateOnum err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("updateOnum close err");
				e.printStackTrace();
			}
		}
	}
	
	public void saveReplyData(BoardBean bean) { //댓글 작성
		String sql = "insert into shopboard values(?,?,?,?,?,?,?,?,?,?,?,?)";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, bean.getNum());
			pstmt.setString(2, bean.getName());
			pstmt.setString(3, bean.getPass());
			pstmt.setString(4, bean.getMail());
			pstmt.setString(5, bean.getTitle());
			pstmt.setString(6, bean.getCont());
			pstmt.setString(7, bean.getBip());
			pstmt.setString(8, bean.getBdate());
			pstmt.setInt(9, 0); //readcnt 조회수, 작성이니까
			pstmt.setInt(10, bean.getGnum()); 
			pstmt.setInt(11, bean.getOnum());
			pstmt.setInt(12, bean.getNested());
			
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("saveReplyData err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("saveReplyData close err");
				e.printStackTrace();
			}
		}
	}
		
	public void saveEditData(BoardBean bean) { //글 수정
		String sql = "update shopboard set name=?,mail=?,title=?,cont=? where num=?";
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, bean.getName());
			pstmt.setString(2, bean.getMail());
			pstmt.setString(3, bean.getTitle());
			pstmt.setString(4, bean.getCont());
			pstmt.setInt(5, bean.getNum());
			
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("saveEditData err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("saveEditData close err");
				e.printStackTrace();
			}
		}
	}
	
	public void delData(String num) { //글 삭제
		String sql = "delete from shopboard where num=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setString(1, num);
			pstmt.executeUpdate();
			
		}catch (Exception e) {
			System.out.println("delData err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("delData close err");
				e.printStackTrace();
			}
		}
	}
	
	public boolean chkPass(int num, String new_pass) { //비밀번호 체크
		boolean b = false;
		String sql = "select pass from shopboard where num=?";
		
		try {
			conn = ds.getConnection();
			pstmt = conn.prepareStatement(sql);
			pstmt.setInt(1, num);
			rs = pstmt.executeQuery();
			
			if(rs.next()) {
				if(new_pass.equals(rs.getString("pass"))) {
					b = true;
				}
			}
		}catch (Exception e) {
			System.out.println("saveEditData err");
			e.printStackTrace();
		}finally {
			try {
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			}catch (Exception e) {
				System.out.println("saveEditData close err");
				e.printStackTrace();
			}
		}
		return b;
	}
	
}
