package pack.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.BoardDaoImpl;
import pack.board.model.BoardDto;

@Controller
public class ListController {
	@Autowired
	private BoardDaoImpl dao;
	
	@RequestMapping("boardlist")
	public ModelAndView list() {
		List<BoardDto> list = dao.getDataAll();
		return new ModelAndView("list", "list", list);
	}
}
