package pack2;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class HappyController {
	
	@RequestMapping(value = "happy", method = RequestMethod.POST)
	public ModelAndView happy() {
		ModelAndView modelAndView = new ModelAndView("view2");
		modelAndView.addObject("message", "웃어");
		return modelAndView;
	}
}
