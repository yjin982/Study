package pack.board.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import pack.board.controller.BoardBean;

@Repository
public class BoardDaoImpl extends SqlSessionDaoSupport implements BoardDaoInter{
	
	@Autowired
	public BoardDaoImpl(SqlSessionFactory factory) {
		setSqlSessionFactory(factory);
	}
	
	public List<BoardDto> getDataAll(){ //게시글 전체 가져오기
		return getSqlSession().selectList("selectDataAll");
	}
	
	public List<BoardDto> getSearch(BoardBean bean){ //검색 결과 가져오기
		return getSqlSession().selectList("selectSearch", bean);
	}
	
	public BoardDto selectDetail(String num) { //글 보기
		return getSqlSession().selectOne("selectDetail", num);
	}

	public void addReadcnt(String num) { //글 보기 전 조회수 증가
		getSqlSession().update("addReadcnt", num);
	}
	
	public int insertData(BoardBean bean) { //글쓰기
		try {
			getSqlSession().insert("insertData", bean);
			return 1;
		}catch (Exception e) {
			System.out.println("insertData err " + e);
			return 0;
		}
	}
	
	public int updateData(BoardBean bean) { //글수정
		try {
			getSqlSession().update("updateData", bean);
			return 1;
		}catch (Exception e) {
			System.out.println("updateData err " + e);
			return 0;
		}
	}
	
	public int deleteData(String num) { //글삭제
		try {
			getSqlSession().delete("deleteData", num);
			return 1;
		}catch (Exception e) {
			System.out.println("deleteData err " + e);
			return 0;
		}
	}
}
