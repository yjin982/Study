package pack.board.controller;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import pack.board.model.BoardDaoImpl;
import pack.board.model.BoardDto;

@Controller
public class DetailController {
	@Autowired
	private BoardDaoImpl dao;
	
	@RequestMapping("detail")
	public ModelAndView detail(@RequestParam("num") String num) {
		dao.addReadcnt(num);  /// 조회수 늘리기
		BoardDto dto = dao.selectDetail(num);
		return new ModelAndView("detail", "data", dto);
	}
}
