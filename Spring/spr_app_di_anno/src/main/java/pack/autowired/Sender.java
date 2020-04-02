package pack.autowired;

import org.springframework.stereotype.Component;

//@Component("sender") // 와 같은 이름으로 객체가 생성
@Component //xml에서 객체 생성하는 것이 아니라 여기에서 스스로 객체생성하게 하는 어노테이션
public class Sender implements SenderInter{ //포함관계로 불러쓰기 위한 클래스
	public void show() {
		System.out.println("sender의 show 메소드 수행");
	}
}
