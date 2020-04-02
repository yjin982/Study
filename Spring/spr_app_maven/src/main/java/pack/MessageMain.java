package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MessageMain {
	public static void main(String[] args) {
		//Spring을 사용하지 않는 경우
		Message1 message1 = new Message1();
		MessageInter inter;
		inter = message1;
		inter.sayHello("홍길동");
		
		/////////////////////////////////////////////////
		//Spring을 사용한 경우 (1. xml 의존적인 경우)
		ApplicationContext context = new ClassPathXmlApplicationContext("init.xml");
		MessageInter inter2 = (MessageInter)context.getBean("mes");
		inter2.sayHello("심춘향");
	}
}
