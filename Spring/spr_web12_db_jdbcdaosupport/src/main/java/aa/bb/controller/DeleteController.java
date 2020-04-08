package aa.bb.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;

import aa.bb.model.MemberDao;

@Controller
public class DeleteController {
	
	@Autowired
	private MemberDao memberDao;
	
	@RequestMapping(value = "delete", method = RequestMethod.GET)
	public String del(@RequestParam("id") String id) {
		memberDao.delData(id);
		return "redirect:/list";
	}
}
