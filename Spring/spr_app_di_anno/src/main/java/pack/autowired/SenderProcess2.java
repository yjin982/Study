package pack.autowired;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Scope;
import org.springframework.stereotype.Service;

@Service("korea")
@Scope("singleton") //singleton 기본값
@ComponentScan("pack.autowired2") //xml파일에서 안 써줘도 여기서 이렇게 스캔을 하는 것이 가능
public class SenderProcess2 { //sender의 부모인 인터페이스를 인젝션
	@Autowired
	@Qualifier("s2") //Sender2를 매핑하라는 뜻
	private SenderInter inter;  


//	public SenderInter getInter() {
//		return inter;
//	}
	
	public void dispData() {
		inter.show();
	}
}
