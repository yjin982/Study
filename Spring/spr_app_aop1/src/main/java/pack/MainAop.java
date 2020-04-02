package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainAop {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_init.xml");
		
		
		/////AOP 적용 전
//		MessageInter inter = context.getBean("messageImpl", MessageInter.class);
//		inter.sayHi();
		
		
		/////AOP 적용 후
		MessageInter inter= (MessageInter)context.getBean("proxy"); 
		inter.sayHi();
		//aop 필요 없다면 proxy가 아니라 messageImpl를 써주면 됨
		//필요하면 넣어주고 필요없으면 쉽게 뺄 수 있어야 하는 것
	}
}
