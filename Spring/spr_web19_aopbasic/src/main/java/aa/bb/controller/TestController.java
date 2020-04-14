package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.MyModelInter;

@Controller
public class TestController {
	@Autowired
	@Qualifier("myModel") //inter의 자식클래스가 2개 이상일 수도 있으니 걸어주는 것이 좋음
	private MyModelInter inter;
	
	
	@RequestMapping("test")
	public ModelAndView aaa() {
		ModelAndView view = new ModelAndView();
		
		String result1 = inter.processMsg();  //모델과 연동한 핵심 메소드
		String result2 = inter.businessMsg();
		
		view.addObject("data1", result1);
		view.addObject("data2", result2);
		view.setViewName("list");
		
		return view;
	}
}
