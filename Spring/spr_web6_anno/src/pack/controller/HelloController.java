package pack.controller;

import java.util.HashMap;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import pack.model.HelloModel;

@Controller
@RequestMapping({"/abc/world", "h*"})
public class HelloController{
	@Autowired
	private HelloModel helloModel;
	
	/** ModelAndView
	@RequestMapping(method = RequestMethod.GET)
	public ModelAndView abc() {
		String result = helloModel.getGreeting();
		ModelAndView modelAndView = new ModelAndView();
		
		modelAndView.setViewName("hello");
		modelAndView.addObject("result", result);
		return modelAndView;
	}
	**/
	/** hashmap을 리턴이기 때문에 view파일명을 지정x, 요청명이 viewfile명이 되어서 hello만 됨
	@RequestMapping(method = RequestMethod.GET)
	public Map<String, Object> abc() {
		String result = helloModel.getGreeting();
		
		HashMap<String, Object> map = new HashMap();
		map.put("result", result);
		return map;
	}
	**/
	/** hashmap과 유사 **/
	@RequestMapping(method = RequestMethod.GET)
	public Model abc(Model model) {
		String result = helloModel.getGreeting();
		
		model.addAttribute("result", result);
		return model;
	}
	
}