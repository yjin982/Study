package aa.bb.cc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Service;
import org.springframework.validation.BindingResult;
import org.springframework.validation.annotation.Validated;
import org.springframework.web.bind.WebDataBinder;
import org.springframework.web.bind.annotation.InitBinder;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@Controller
@Service //가독성을 위해서 서비스를 같이 주는 경우 있음
public class LoginController {
	private String formViewName = "loginform";
	
	@Autowired
	private LoginCommand loginCommand;
	
	
	@ModelAttribute("command")
	public LoginCommand formBack() {
		return loginCommand; // or return new LoginCommand();
	}
	
	@RequestMapping(value = "login", method = RequestMethod.GET)
	public String form() {	
		return formViewName; //or return "loginform", view 파일명을 리턴
	}
	
	/**
	@RequestMapping(value = "login", method = RequestMethod.POST)
	public String submit(LoginCommand loginCommand) { //loginform.jsp 에서 전송버튼을 타고 정보(폼빈)가 들어옴
		if(loginCommand.getUserid().equals("aa") && loginCommand.getPasswd().equals("11")) {
			return "redirect:/list";  //리다이렉트로 목록보기(클라이언트를 통해서 list요청이 들어온것과 같음 == login요청처럼)
		}else {
			return formViewName; //틀리면 그냥 그대로 로그인 화면창으로 돌아가게
		}
	}
	**/
	/**로그인 입력값을 체크해는거 추가**/
	@RequestMapping(value = "login", method = RequestMethod.POST)
	public String submit(@Validated @ModelAttribute("command") LoginCommand loginCommand, BindingResult bindingResult) { 
		if(loginCommand.getUserid().equals("aa") && loginCommand.getPasswd().equals("11")) {
			return "redirect:/list";
		}else {
			return formViewName;
		}
	}
	@InitBinder //BindingResult와 연결
	public void initBinder(WebDataBinder binder) {
		binder.setValidator(new DataValidator());
	}
}
