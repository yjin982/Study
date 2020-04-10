package pack.board.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.BoardDaoImpl;
import pack.board.model.BoardDto;

@Controller
public class SearchController {
	@Autowired
	private BoardDaoImpl dao;

	@RequestMapping("search")
	public ModelAndView search(BoardBean bean) {
		List<BoardDto> list = dao.getSearch(bean);
		return new ModelAndView("list", "list", list);
	}
}
