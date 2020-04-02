package pack.autowired;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

//@Component("aa")
@Service   //@Component 라는 어노테이션은 다른데서 불려지는 객체, 실제 로직을 실행하는 클래스라면 service를 사용 (둘다 객체를 생성하는 역할이나 가독성(혹은 역할 구분) 문제)
public class SenderProcess { //sender 클래스 자체를 인젝션
	@Autowired  // 내무적으로 setter 메소드를 만들어서 운영. ★★ type에 의한 mapping ★★
	private Sender sender;  
	////private 멤버에 setter 를 연결하는 것은 당연한 이야기이기 때문에 이를 자동으로 해준다는 뜻
	////주의, 인터페이스를 걸어버리면 인터페이스 아래에 여러개의 자식이 있을 경우 어떤 자식을 연결해주는지 찾지 못함.
	
	
	/*
	public void setSender(Sender sender) {
		this.sender = sender;
	}
	*/
//	public Sender getSender() {
//		return sender;
//	}
	
	public void dispData() {
		sender.show();
	}
}
