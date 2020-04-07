package aa.bb.cc;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class LoginController {
	
	@RequestMapping(value = "kbs/login", params = "type=admin")
	public ModelAndView aaa() {
		ModelAndView modelAndView = new ModelAndView("show");
		modelAndView.addObject("message", "관리자입니다");
		return modelAndView;
	}
	@RequestMapping(value = "kbs/login", params = "type=user")
	public ModelAndView bbb() {
		ModelAndView modelAndView = new ModelAndView("show");
		modelAndView.addObject("message", "일반 고객");
		return modelAndView;
	}
	@RequestMapping(value = "kbs/login", params = "!type") //type이 없다
	public ModelAndView ccc() {
		ModelAndView modelAndView = new ModelAndView("show");
		modelAndView.addObject("message", "파라미터가 읎네요");
		return modelAndView;
	}
	
	/** 요청 url 일부를 정보로 얻기 **/
	@RequestMapping(value = "kbs/{url}")
	public ModelAndView dd(@RequestParam("type") String type, @PathVariable String url) {
//		ModelAndView modelAndView = new ModelAndView("show");
//		modelAndView.addObject("message", "기타 : " + type + ", url : " + url);
//		return modelAndView;
		
		ModelAndView modelAndView = new ModelAndView("show");
		if(url.equals("login")) {
			modelAndView.addObject("message", type);
		}else if(url.equals("korea")) {
			modelAndView.addObject("message", "대한민국 만세");
		}else{
			modelAndView.addObject("message", "기타");
		}
		return modelAndView;
	}
	
	/** 요청 url로 정보로 얻기 **/
	@RequestMapping(value = "ent/{com}/singer/{singer}")	
	public ModelAndView eee(@RequestParam("title") String title, @PathVariable("com") String so, @PathVariable String singer) {
		ModelAndView modelAndView = new ModelAndView("show");
		String ss = "소속사 : " + so + ", 가수 : " + singer + ", 곡명 : " + title;
		modelAndView.addObject("message", ss);
		return modelAndView;
	}
}
