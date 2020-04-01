package pack.mybatis;

import java.io.Reader;

import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

public class SqlMapConfig {
	public static SqlSessionFactory sqlSession; // sql 사용시 필요 메소드를 가지고 있음. (Factory= 스스로 new)
	
	static {
		String source = "pack/mybatis/Configuration.xml";
		
		try {
			Reader reader = Resources.getResourceAsReader(source); //설정파일을 읽어서
			sqlSession = new SqlSessionFactoryBuilder().build(reader); //세션으로 넘겨줌(웹에서의 세션 X, 하나의 작업단위)
			reader.close();
			
		}catch (Exception e) {
			System.out.println("SqlMapConfig err");
			e.printStackTrace();
		}
	}
	
	public static SqlSessionFactory getSqlSession() { 
		return sqlSession;
	}
}//마이바티스 샘플에 써있는 대로임
