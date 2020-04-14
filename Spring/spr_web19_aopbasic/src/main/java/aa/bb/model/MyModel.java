package aa.bb.model;

import org.springframework.stereotype.Repository;

//@Component 현상태에선 이거도 괜찮으나 db다녀온다 가정하고 레파지토리
@Repository
public class MyModel implements MyModelInter {
	//핵심 로직은 db를 가든 안 가든 모델에 있음
	
	@Override
	public String processMsg() {
		System.out.println("processMsg 핵심 메소드 수행");
		return "Spring Aop 다오";
	}
	
	@Override
	public String businessMsg() {
		System.out.println("businessMsg 핵심 메소드 수행");
		return "나이스한 Spring Aop";
	}
}
