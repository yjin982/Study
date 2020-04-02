package pack.autowired2;

import org.springframework.stereotype.Component;

import pack.autowired.SenderInter;

@Component("s2")  //SenderProcess2에서는 s2라는 이름으로 참조하기때문에 s2라는 이름으로 객체 생성
public class Sender2 implements SenderInter{ 
	public void show() {
		System.out.println("sender의 show 메소드 수행 : Sender2");
	}
}
