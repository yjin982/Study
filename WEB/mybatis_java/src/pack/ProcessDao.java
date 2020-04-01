package pack;

import java.sql.SQLException;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;

public class ProcessDao {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession(); //
	
	
	public List selectSangDataAll() throws SQLException{ //DB전체 읽기 select *
		SqlSession sqlSession = factory.openSession();
		List list = sqlSession.selectList("selectDataAll"); //dataMapper.xml의 id
		sqlSession.close();
		
		return list;
	}
	
	/////부분읽기
	public DataDto selectDataPart(String arg) throws SQLException{ //try catch로 잡을 수도 있음
		SqlSession sqlSession = factory.openSession();
		DataDto dto = sqlSession.selectOne("selectDataPart", arg); //arg가 sql에서 코드번호 주는것
		sqlSession.close();
		
		return dto;
	}
	
	/////추가
	public void insData(DataDto dto) throws Exception {
		SqlSession sqlSession = factory.openSession();      //수동 commit : commit 없으면 db에 반영 안됨. 
//		SqlSession sqlSession = factory.openSession(true); //자동 commit
		sqlSession.insert("insertData", dto);
		sqlSession.commit(); //sqlSession.rollback();
		sqlSession.close();
	}
	
	/////수정
	public void upData(DataDto dto) throws Exception {
		SqlSession sqlSession = factory.openSession(true);
		sqlSession.update("upData", dto);
		sqlSession.close();
	}
	
	/////삭제
	public boolean deleteData(int arg){
		SqlSession sqlSession = factory.openSession();
		boolean re = false;
		
		try {
			int cou = sqlSession.delete("delData", arg); //성공하면 1 실패하면 0 반환
			if(cou > 0) re = true;
			sqlSession.commit();
			
		} catch (Exception e) {
			System.out.println("deleteData err " + e);	
			sqlSession.rollback();
			
		}finally {
			if(sqlSession != null) sqlSession.close();			
		}
		return re;
	}
}
