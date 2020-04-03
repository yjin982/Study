package pack3;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Service;


@Service
public class LogicImpl implements LogicInter{
	//핵심 로직
	@Autowired          //생성자 대신에 setter 인젝션 어노테이션 사용
	@Qualifier("articleDao")
	private ArticleInter articleInter;
	
	public LogicImpl() {}
	
	public void selectDataProcess() {
		articleInter.selectAll();
	}
	
	public void updateDataPart() {
		System.out.println("updateDataPart 수행");
	}
	
	public void etc() {
		System.out.println("다른 작업이 더 있을 수 있음");
	}
}
