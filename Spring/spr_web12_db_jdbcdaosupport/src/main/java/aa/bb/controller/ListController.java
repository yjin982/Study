package aa.bb.controller;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.model.MemberDao;
import aa.bb.model.MemberDto;

@Controller
public class ListController {
	@Autowired
	private MemberDao memberDao;
	
	/** 페이징 처리 전
	@RequestMapping("list")
	public ModelAndView listProcess() {
		ModelAndView view = new ModelAndView();
		List<MemberDto> list = memberDao.getMemberAll();   //모델 영역의 클래스와 통신
		view.setViewName("list");
		view.addObject("list", list);
		return view;
	}
	**/
	private int pageSize = 3; //페이지당 출력 행 수
	
	@RequestMapping("list")  //http:// ~ /list?pageNum=1
	public ModelAndView listProcess(@RequestParam(value="pageNum", defaultValue="1") String pageNum) {
		int currentPage = Integer.parseInt(pageNum);
		int startRow = (currentPage - 1) * pageSize; // 0, 3, 6, ...
		int endRow = pageSize;  //출력시킬 갯수
		int count = memberDao.getMemberCount();  //페이지 번호 링크 달기 위한
		
		ModelAndView view = new ModelAndView();
		List<MemberDto> list = memberDao.getMemberAll(startRow, endRow);   //모델 영역의 클래스와 통신
		view.setViewName("list");
		view.addObject("currentPage", currentPage);
		view.addObject("count", count);
		view.addObject("pageSize", pageSize);
		view.addObject("list", list);
		return view;
	}
}
