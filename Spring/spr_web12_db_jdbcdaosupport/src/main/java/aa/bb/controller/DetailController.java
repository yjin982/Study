package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.MemberDao;
import aa.bb.model.MemberDto;

@Controller
public class DetailController {
	@Autowired
	private MemberDao memberDao;
	
	@RequestMapping("detail")
	public ModelAndView detailProcess(@RequestParam("id") String id) {
		MemberDto dto = memberDao.getMember(id);
		return new ModelAndView("detail", "member", dto);
	}
}
