package pack;

import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class MessageMain2 {
	//@Configuration 어노테이션을 적용한 환경파일 읽기 
	public static void main(String[] args) {
		AnnotationConfigApplicationContext context = new AnnotationConfigApplicationContext(Config.class);
		
		MessageInter inter2 = context.getBean("messageImpl", MessageInter.class);
		inter2.sayHi();
	}
}
