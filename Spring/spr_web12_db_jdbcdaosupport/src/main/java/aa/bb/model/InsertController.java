package aa.bb.model;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import aa.bb.controller.MemberBean;

@Controller
public class InsertController {
	@Autowired
	private MemberDao memberDao;
	private String formName = "insform";
	
	@ModelAttribute("command")
	public MemberBean formBack() {
		return new MemberBean();
	}
	
	@RequestMapping(value = "insert", method = RequestMethod.GET)
	public String form() {
		return formName;
	}
	
	@RequestMapping(value = "insert", method = RequestMethod.POST)
	public String form(MemberBean bean) {
		memberDao.insData(bean);
		return "redirect:/list";
	}
}
