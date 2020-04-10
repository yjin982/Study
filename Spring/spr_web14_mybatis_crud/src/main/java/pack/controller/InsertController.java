package pack.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import pack.model.MemDaoInter;

@Controller
public class InsertController {
	@Autowired
	@Qualifier("memDaoImpl")
	private MemDaoInter daoInter;
	
	@RequestMapping(value = "insert", method = RequestMethod.GET)
	public String list() {
		return "insform";
	}

	@RequestMapping(value = "insert", method = RequestMethod.POST)
	public String submit(MemBean bean) {
		boolean b = daoInter.insertData(bean);
		
		if(b) {
			return "redirect:/list";   //추가 후 목록 보기
		}else {
			return "error";
		}
	}
}
