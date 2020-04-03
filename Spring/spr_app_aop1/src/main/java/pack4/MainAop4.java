package pack4;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;


public class MainAop4 {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_init4.xml");
		
		LogicInter logicInter = (LogicInter)context.getBean("logicImpl");
		logicInter.startProcess();
	}
}
