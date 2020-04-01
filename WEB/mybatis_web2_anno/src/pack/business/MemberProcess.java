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
			SqlMapperInter inter = (SqlMapperInter)sqlSession.getMapper(SqlMapperInter.class); //object으로 주기때문에 인터페이스로 캐스팅
			list = inter.selectDataAll(); // 인터페이스가 sql문을 전달...?
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
			 SqlMapperInter inter = (SqlMapperInter)sqlSession.getMapper(SqlMapperInter.class); 
			 if(inter.insertData(bean) > 0) b = true;
			 
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
			SqlMapperInter inter = (SqlMapperInter)sqlSession.getMapper(SqlMapperInter.class);
			dto = inter.selectDataPart(id);
			
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
			SqlMapperInter inter = (SqlMapperInter)sqlSession.getMapper(SqlMapperInter.class); 
			//비밀번호 비교 후 수정여부를 판단
			DataDto dto = inter.selectDataPart(bean.getId());
			
			if(dto.getPasswd().equalsIgnoreCase(bean.getPasswd())) {
				if(inter.updateData(bean) > 0) {
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
			SqlMapperInter inter = (SqlMapperInter)sqlSession.getMapper(SqlMapperInter.class); 
			int cou = inter.deleteData(id);
			
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
