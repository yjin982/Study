package pack.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import pack.model.SangpumInter;

@Controller
@ComponentScan("pack.model")
public class SearchController {
	@Autowired
	@Qualifier("sangpumImpl")
	private SangpumInter inter;
	
	@RequestMapping(value = "search", method = RequestMethod.POST)
	public ModelAndView searchProcess(SangpumBean bean) {
		return new ModelAndView("list", "datas", inter.search(bean));
	}

}
