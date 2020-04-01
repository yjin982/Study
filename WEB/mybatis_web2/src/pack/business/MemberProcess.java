package pack.business;

import java.util.List;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import pack.mybatis.SqlMapConfig;


public class MemberProcess {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession();
	
	public List<DataDto> selectDataAll(){ //전체 자료 select
		SqlSession sqlSession = factory.openSession();
		List<DataDto> list = null;
		
		try {
			list = sqlSession.selectList("selectDataAll");
		}catch (Exception e) {
			System.out.println("selectDataAll err " + e);
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		return list;
	}
	
	public boolean insertData(DataFormBean bean) { //데이터 입력
		SqlSession sqlSession = factory.openSession();
		boolean b = false;
		
		 try {
			 if(sqlSession.insert("insertData", bean) > 0) b = true;
			 sqlSession.commit();
		 }catch (Exception e) {
			System.out.println("insertData err " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		
		return b;
	}
	
	public DataDto selectDataPart(String id) { //데이터 부분 select(일부만 가져오기)
		SqlSession sqlSession = factory.openSession();
		DataDto dto = null;
		
		try {
			dto = sqlSession.selectOne("selectDataPart",id);
			
		}catch (Exception e) {
			System.out.println("selectDataPart err " + e);

		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		
		return dto;
	}
	
	public boolean updateData(DataFormBean bean) { //데이터 수정
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		bean.setColname("id");
		
		try {
			//비밀번호 비교 후 수정여부를 판단
			DataDto dto = selectDataPart(bean.getId());
			if(dto.getPasswd().equalsIgnoreCase(bean.getPasswd())) {
				if(sqlSession.update("upData", bean) > 0) {
					b = true;
					sqlSession.commit();						
				}				
			}
		}catch (Exception e) {
			System.out.println("updateData err " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		
		return b;
	}
	
	public boolean deleteData(String id) {
		boolean b = false;
		SqlSession sqlSession = factory.openSession();
		
		try { //비밀번호 검사 생략
			int cou = sqlSession.delete("delData", id);
			if(cou > 0) b = true; 
			sqlSession.commit();
		}catch (Exception e) {
			System.out.println("deleteData err " + e);
			sqlSession.rollback();
		}finally {
			if(sqlSession != null) sqlSession.close();
		}
		
		return b;
	}
}
