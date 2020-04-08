package aa.bb.cc;

import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

@Controller
public class ListController {
	@RequestMapping("list")
	public String successLogin(Model model) {
		String msg = "로그인 성공으로 비즈니스 로직 수행됨";
		model.addAttribute("msg", msg);
		return "show";  //show.jsp 부르기
	}
}
