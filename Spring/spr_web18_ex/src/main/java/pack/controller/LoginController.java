package pack.controller;

import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

@Controller
public class LoginController {
	@RequestMapping(value = "login", method = RequestMethod.GET)
	public String login(HttpSession session) {
		if(session.getAttribute("id") == null) {
			return "login";   //로그인 상태가 아니면 로그인 화면
		}else {
			return "redirect:/list"; //아니면 부서화면 보이기
		}
	}
	
	@RequestMapping(value = "login", method = RequestMethod.POST)
	public String loginProcess(HttpSession session, @RequestParam("id") String id, @RequestParam("pw") String pw) {
		if(id.equals("aa") && pw.equals("11")) { //원래는 db 갔다 오는걸로 처리해야
			session.setAttribute("id", id);
			return "redirect:/list"; //클라이언트 요청으로 가야 데이터가 뜸
		}else {
			return "redirect:/err.jsp";
		}
	}
	
	////////////////////////////////////////////////////////////////////////////////////
	@RequestMapping(value = "logout", method = RequestMethod.GET)
	public String logout(HttpSession session) {
		session.invalidate();
		return "redirect:/index.jsp";
	}
}
