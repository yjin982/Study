package pack2;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainAop2 {
	public static void main(String[] args) {
		ApplicationContext context = new ClassPathXmlApplicationContext("aop_init2.xml");
		
		LogicInter inter = context.getBean("logicImpl", LogicInter.class);
		inter.selectDataProcess();
		inter.updateDataPart();
	}
}
