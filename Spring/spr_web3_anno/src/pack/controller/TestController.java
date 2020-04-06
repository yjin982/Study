package pack.controller;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class TestController {
	
	@RequestMapping("start.do")
	public ModelAndView mbc() {
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.addObject("key", "어노테이션으로 처리");
		modelAndView.setViewName("list");
		return modelAndView;
	}
}
