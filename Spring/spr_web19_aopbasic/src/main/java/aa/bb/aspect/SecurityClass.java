package aa.bb.aspect;

import org.springframework.stereotype.Component;

@Component
public class SecurityClass { //관심사항 중 보안 관련
	
	public void MySecurity() {
		System.out.println("핵심 메소드 전에 보안 작업 실행");
	}
}
