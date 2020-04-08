package aa.bb.controller;

import java.util.ArrayList;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import aa.bb.Model.DataDao;
import aa.bb.Model.SangpumDto;

@Controller
public class ListController {
	@Autowired
	private DataDao dataDao;
	
	@RequestMapping("testdb")
	public ModelAndView listProcess() {
		//모델과 통신 가능
		ArrayList<SangpumDto> list = dataDao.getDataAll();
		//if list가 null이면 나올 화면, 아니면 데이터 출력할 화면 구분할 수 있음
		return new ModelAndView("show", "datas", list);
	}
}
