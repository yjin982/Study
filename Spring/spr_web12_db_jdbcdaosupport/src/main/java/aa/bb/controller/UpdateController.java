package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.MemberDao;
import aa.bb.model.MemberDto;

@Controller
public class UpdateController {
	@Autowired
	private MemberDao memberDao;
	
	private String formName = "upform";
	
	@RequestMapping(value = "update", method = RequestMethod.GET)
	public ModelAndView form(@RequestParam("id") String id) { //insert할때 databean을 만들어서 여기서는 만들 필요가 없음
		MemberDto dto = memberDao.getMember(id);
		return new ModelAndView(formName, "updata", dto);
	}
	
	@RequestMapping(value = "update", method = RequestMethod.POST)
	public String submit(MemberBean bean) { //insert할때 databean을 만들어서 여기서는 만들 필요가 없음
		memberDao.upData(bean);
		return "redirect:/list";
	}
}
