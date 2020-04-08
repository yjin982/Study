package aa.bb.cc;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class Sub2Controller {
	
	@RequestMapping(value = "/sub2", method = RequestMethod.GET)
	public ModelAndView def(HttpServletRequest request) {
		String para = request.getParameter("irum");
			
		if(para.equals("tom")) {
			String msg = para + "님 반가워요!";
			return new ModelAndView("sub_list2", "msg", msg);
		}else {
			return new ModelAndView("redirect:/resources/index.html");			
		}
		
	}
}
