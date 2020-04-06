package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HelloController{
	
	@RequestMapping("hello.do") //get, post 둘 다 적용
	public ModelAndView abc() {
		ModelAndView modelAndView = new ModelAndView();
	
		modelAndView.setViewName("view1");
		modelAndView.addObject("message", "Hello annotation!");
		return modelAndView;
	}
}
