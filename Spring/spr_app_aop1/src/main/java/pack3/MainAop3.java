package pack3;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainAop3 {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_init3.xml");
		
		LogicInter inter = (LogicInter)context.getBean("logicImpl");
		inter.selectDataProcess();
		inter.updateDataPart();
	}
}
