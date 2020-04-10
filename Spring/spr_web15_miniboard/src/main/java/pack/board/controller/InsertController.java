package pack.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

import pack.board.model.BoardDaoImpl;

@Controller
public class InsertController {
	@Autowired
	BoardDaoImpl dao;
	
	@RequestMapping(value = "insert", method = RequestMethod.GET)
	public String insert() {
		return "insform";
	}
	
	@RequestMapping(value = "insert", method = RequestMethod.POST)
	public String submit(BoardBean bean) {
		int re = dao.insertData(bean);
		
		if(re > 0)
			return "redirect:/boardlist";  ////추가 후 목록보기 요청
		else
			return "error";	//// forwarding으로 error.jsp 호출
	}
}
