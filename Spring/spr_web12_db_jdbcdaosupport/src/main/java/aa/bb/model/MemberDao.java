package aa.bb.model;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.jdbc.core.RowMapper;
import org.springframework.jdbc.core.support.JdbcDaoSupport;
import org.springframework.jdbc.datasource.DriverManagerDataSource;
import org.springframework.stereotype.Repository;
import org.springframework.web.bind.annotation.RequestMapping;

import aa.bb.controller.MemberBean;

@Repository
public class MemberDao extends JdbcDaoSupport{
	
	@Autowired
	public MemberDao(DriverManagerDataSource dataSource) {
		setDataSource(dataSource);
	}
	
	/**
	@RequestMapping("list")
	public List<MemberDto> getMemberAll() {
		String sql = "select * from member";
		List<MemberDto> list = getJdbcTemplate().query(sql, new RowMapper() {
			@Override
			public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
				MemberDto dto = new MemberDto();
				dto.setId(rs.getString("id"));
				dto.setName(rs.getString("name"));
				dto.setPasswd(rs.getString("passwd"));
				dto.setRegdate(rs.getString("regdate"));
				return dto;
			}
		});
		return list;
	}
	**/
	/**페이징 처리 추가해서 전체 조회**/
	@RequestMapping("list")
	public List<MemberDto> getMemberAll(int startRow, int endRow) {
		String sql = "select * from member limit ?,?";
		List<MemberDto> list = getJdbcTemplate().query(sql, new Object[] {startRow, endRow}, new RowMapper() {
			@Override
			public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
				MemberDto dto = new MemberDto();
				dto.setId(rs.getString("id"));
				dto.setName(rs.getString("name"));
				dto.setPasswd(rs.getString("passwd"));
				dto.setRegdate(rs.getString("regdate"));
				return dto;
			}
		});
		return list;
	}
	
	/**전체 레코드 수 조회 - paging**/
	public int getMemberCount() {
		String sql = "select count(*) from member";
		return getJdbcTemplate().queryForObject(sql, Integer.class); //값을 하나만 리턴해도 되니까
	}
	
	public void insData(MemberBean bean) { //추가
		String sql = "insert into member values(?, ?, ?, now())";
		Object[] params = {bean.getId(), bean.getPasswd(), bean.getName()};
		getJdbcTemplate().update(sql, params);
	}
	
	public void upData(MemberBean bean) { //수정
		String sql = "update member set passwd=?, name=? where id=?";
		getJdbcTemplate().update(sql, new Object[] {bean.getPasswd(), bean.getName(), bean.getId()});
	}
	
	public void delData(String id) { //삭제
		String sql = "delete from member where id=?";
		getJdbcTemplate().update(sql, new Object[] {id});
	}
	
	/**상세 조회를 위한 레코드 한개 조회**/
	public MemberDto getMember(String id) {
		String sql = "select * from member where id=?";
		MemberDto dto = (MemberDto)getJdbcTemplate().queryForObject(sql, new Object[]	 {id}, new RowMapper() {
			@Override
			public Object mapRow(ResultSet rs, int rowNum) throws SQLException {
				MemberDto dto = new MemberDto();
				dto.setId(rs.getString("id"));
				dto.setName(rs.getString("name"));
				dto.setPasswd(rs.getString("passwd"));
				dto.setRegdate(rs.getString("regdate"));
				return dto;
			}
		});
		return dto;
	}
}
