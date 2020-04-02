package pack;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;
import org.springframework.context.support.GenericApplicationContext;
import org.springframework.context.support.GenericXmlApplicationContext;

public class MessageMain {
	public static void main(String[] args) {
		//ApplicationContext context = new ClassPathXmlApplicationContext("classpath:arrange.xml"); //경로가 main/resources 아래에 있을 경우, 정확하게는 classpath:arrange.xml, 생략가능
		//ApplicationContext context = new ClassPathXmlApplicationContext("classpath:pack/arrange.xml"); //경로가 main/java/pack아래에 있을 경우
		GenericApplicationContext context = new GenericXmlApplicationContext("classpath:pack/arrange.xml");
		
		
		MessageImpl impl1 = (MessageImpl)context.getBean("messageImpl");
		impl1.sayHi();
		MessageImpl impl2 = (MessageImpl)context.getBean("messageImpl");
		impl2.sayHi();
		System.out.println("impl1의 주소 : " + impl1);
		System.out.println("impl2의 주소 : " + impl2);
		/**실행결과 : 
		 * impl1의 주소 : pack.MessageImpl@175b9425
		 * impl2의 주소 : pack.MessageImpl@175b9425
		 * 주소가 일치하다는 것은 싱글톤 패턴이라는 것을 확인할 수 있다.
		 * arrange.xml 의 scope 기본값이 scope="singleton" 임
		 * prototype(프로토타입일때는 주소값이 달라짐), request, session
		 **/
		
		/////다형성
		MessageInter inter1 = (MessageImpl)context.getBean("messageImpl");
		inter1.sayHi();
		MessageInter inter2 = context.getBean("messageImpl", MessageInter.class);
		inter2.sayHi();

	}
}
