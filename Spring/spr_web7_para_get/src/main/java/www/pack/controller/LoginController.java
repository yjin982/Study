package www.pack.controller;

import javax.servlet.http.HttpServletRequest;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

/**방법 1 : legacy적
@Controller
public class LoginController {
	@RequestMapping(value = "login", method = RequestMethod.GET)
	public ModelAndView submit(HttpServletRequest request) {
		String id = request.getParameter("id");
		String pw = request.getParameter("pw");
		String data = "";
		
		if(id.equals("aa") && pw.equals("11")) {
			data = "로그인 성공!";
		}else {
			data = "땡! 실패!";
		}
		
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("result");
		modelAndView.addObject("data", data);
		
		return modelAndView;
	}
}
**/

/**방법 2 : @RequestParam **/
@Controller
@RequestMapping("login")
public class LoginController {
	@RequestMapping(method = RequestMethod.GET)
	public ModelAndView submit(@RequestParam("id") String id, @RequestParam("pw") int pw) { //text지만 숫자로만 받기도 가능
		String data = "";
		
		if(id.equals("aa") && pw == 11) {
			data = "로그인 성공!";
		}else {
			data = "땡! 실패!";
		}
		
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("result");
		modelAndView.addObject("data", data);
		
		return modelAndView;
	}
}
