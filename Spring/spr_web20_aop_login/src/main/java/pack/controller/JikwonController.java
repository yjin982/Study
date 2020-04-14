package pack.controller;

import java.util.List;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.model.JikwonDto;
import pack.model.JikwonInter;

@Controller
public class JikwonController {
	@Autowired
	@Qualifier("jikwonImpl")
	private JikwonInter inter;
	
	
	@RequestMapping("jikwonList")
	public ModelAndView aa(HttpServletRequest request, HttpServletResponse response) { //aop처리할때는 명시적으로 써줄 필요가 있음!! *순서 중요*
		ModelAndView view = new ModelAndView();
		List<JikwonDto> list = inter.jikwonList();
		
		view.setViewName("list");
		view.addObject("list", list);
		return view;
	}
}
