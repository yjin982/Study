package pack.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import pack.model.SangpumDto;
import pack.model.SangpumInter;


@Controller
@ComponentScan("pack.model")
public class ListController {
	@Autowired
	@Qualifier("sangpumImpl")
	private SangpumInter inter;
	
	@RequestMapping("list")
	public Model process(Model model) {
		List<SangpumDto> list = inter.selectList();
		model.addAttribute("datas", list);
		return model;
	}
}
