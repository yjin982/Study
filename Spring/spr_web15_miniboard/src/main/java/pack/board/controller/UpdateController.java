package pack.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.BoardDaoImpl;

@Controller
public class UpdateController {
	@Autowired
	private BoardDaoImpl dao;
	
	@RequestMapping(value = "upfrm", method = RequestMethod.POST)
	public ModelAndView update(BoardBean bean) { //수정 폼으로 이동
		return new ModelAndView("upform", "data", bean);
	}
	
	@RequestMapping(value = "update", method = RequestMethod.POST)
	public String submit(BoardBean bean) { //수정 진행
		int re = dao.updateData(bean);
		
		if(re > 0)
			return "redirect:/boardlist";
		else
			return "error";
	}
}
