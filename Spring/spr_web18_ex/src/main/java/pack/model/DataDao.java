package pack.model;

import java.util.List;

import org.apache.ibatis.session.SqlSessionFactory;
import org.mybatis.spring.support.SqlSessionDaoSupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

@Repository
public class DataDao extends SqlSessionDaoSupport{
	@Autowired
	public DataDao(SqlSessionFactory factory) {
		setSqlSessionFactory(factory);
	}
	
	public List<BuserDto> buserList(){
		List<BuserDto> list = getSqlSession().selectList("showBuser");
		return list;
	}
	
	public List<JikwonDto> jikwonList(String buser_num){
		List<JikwonDto> list = getSqlSession().selectList("showJikwon", buser_num);
		return list;
	}
	
	public int hasGogek(String num) {
		int no = getSqlSession().selectOne("ishaveGogek", num);
		return no;
	}
}
