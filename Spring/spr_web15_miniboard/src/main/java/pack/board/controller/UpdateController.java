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
	public ModelAndView update(BoardBean bean) {
		return new ModelAndView("upform", "data", bean);
	}
	
	@RequestMapping(value = "update", method = RequestMethod.POST)
	public String submit(BoardBean bean) {
		int re = dao.updateData(bean);
		
		if(re > 0)
			return "redirect:/boardlist";  ////추가 후 목록보기 요청
		else
			return "error";	//// forwarding으로 error.jsp 호출
	}
}
