package pack;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class WorldController {

//	@RequestMapping("world.do")
	@RequestMapping(value = {"world.do","good.do","nice*","day"}, method = RequestMethod.GET) //get일 때
	//"{world.do,good.do,nice.do,day}" 로 해도 돼더라; 확장자 없어도 됨, 파일명으로 매핑
	public ModelAndView def() {
		ModelAndView modelAndView = new ModelAndView();
	
		modelAndView.setViewName("view2");
		modelAndView.addObject("message", "GET annotation world!");
		return modelAndView;
	}
	
	@RequestMapping(value = "world.do", method = RequestMethod.POST) //post일 때
	public ModelAndView xyz() {
		ModelAndView modelAndView = new ModelAndView();
	
		modelAndView.setViewName("view2");
		modelAndView.addObject("message", "POST anno WORLD!");
		return modelAndView;
	}
}
