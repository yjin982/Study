package pack.controller;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class MainSelect {

	public static void main(String[] args) {
		//Spring이 작성한 객체를 읽어서 실행
		ApplicationContext context = new ClassPathXmlApplicationContext("select_init.xml");
		
		SelectService selectService = (SelectService)context.getBean("selectServiceImpl"); //스프링이 생성한 객체는 모드 오브젝트 타입이므로 캐스팅
		selectService.selectProcess();
	}

}
