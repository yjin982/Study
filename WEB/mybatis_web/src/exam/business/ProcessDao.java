package exam.business;

import java.sql.SQLException;
import java.util.List;

import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import exam.mybatis.SqlMapConfig;

public class ProcessDao {
	private SqlSessionFactory factory = SqlMapConfig.getSqlSession(); //
	
	
	public List selectJikwonAll(){
		SqlSession sqlSession = factory.openSession();
		JikwonFormbean jbean = new JikwonFormbean();
		jbean.setJik1("과장");
		jbean.setJik2("대리");
		List list = null;

		try {
			list = sqlSession.selectList("selectJikwonAll", jbean);
			
		} catch (Exception e) {
			System.out.println("selectJikwonAll err " + e);	
		}finally {
			if(sqlSession != null) sqlSession.close();			
		}

		return list;
	}
	

	public JikwonPayDto selectJikwonSu(String jik){ //원하는 직급 하나만 가져오는 거
		SqlSession sqlSession = factory.openSession();
		JikwonPayDto dto = null;
		
		try {
			dto = sqlSession.selectOne("selectJikwonSu", jik);
		}catch (Exception e) {
			System.out.println("selectJikwonSu err " + e);	
		}finally {
			if(sqlSession != null) sqlSession.close();			
		}
		//System.out.println(dto.getJikwon_jik() + " " + dto.getJsu() + " " + dto.getJsum() + " " + dto.getJavg());
		sqlSession.close();
		
		return dto;
	}
	
	
	public List selectJikwonPay() { //전체 직급별로 가져오는거
		SqlSession sqlSession = factory.openSession();
		JikwonFormbean jbean = new JikwonFormbean();
		jbean.setJik1("과장");
		jbean.setJik2("대리");
		List list = null;

		try {
			list = sqlSession.selectList("selectJikwonPay");
			
		} catch (Exception e) {
			System.out.println("selectJikwonAll err " + e);	
		}finally {
			if(sqlSession != null) sqlSession.close();			
		}

		return list;
	}
	
	
}
