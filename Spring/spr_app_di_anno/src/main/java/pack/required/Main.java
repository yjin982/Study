package pack.required;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {
	public static void main(String[] args) {
		AbstractApplicationContext context = new ClassPathXmlApplicationContext("anno1.xml");
		
		Abc abc = context.getBean("abc", Abc.class);
		System.out.println(abc.showData());
		
		context.registerShutdownHook(); //서블릿 destory()를 명시적으로 호출
		context.refresh();
		context.close(); // 스프링 컨테이너 종료시 모든 빈의 종료를 수행. Spring @MVC 에서는 이 작업이 자동.
	}
}
