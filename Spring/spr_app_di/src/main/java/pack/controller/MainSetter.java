package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainSetter {

	public static void main(String[] args) {
		//Spring이 작성한 객체를 읽어서 실행
		ApplicationContext context = new ClassPathXmlApplicationContext("setter_init.xml");
		
		SetterProcess process = (SetterProcess)context.getBean("setterProcess");
		process.showData();
	}

}
