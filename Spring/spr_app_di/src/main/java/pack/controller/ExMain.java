package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class ExMain {
	
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("ex_init.xml");
		
		ExfirstService exam =(ExfirstService)context.getBean("firstServiceImpl");
		exam.showData();
	}
}
