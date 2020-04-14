package pack.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;
import org.springframework.web.servlet.ModelAndView;

import pack.model.BuserDto;
import pack.model.DataDao;

@Controller
public class BuserController {
	@Autowired
	private DataDao dao;
	
	/*
	@RequestMapping("buser")
	@ResponseBody
	public Map<String, Object> buserFunc(){
		List<Map<String, String>> dataList = new ArrayList<Map<String,String>>();
		Map<String, String> data = null;
		
		List<BuserDto> bu = dao.buserList();
		for(BuserDto dto : bu) {
			data = new HashMap<String, String>();
			data.put("buser_no", dto.getBuser_no());
			data.put("buser_name", dto.getBuser_name());
			data.put("buser_tel", dto.getBuser_tel());
			dataList.add(data);
		}
		
		Map<String, Object> busers = new HashMap<String, Object>();
		busers.put("b", dataList);
		return busers;
	}*/
	
	@RequestMapping("list")
	public ModelAndView buser() {
		return new ModelAndView("list", "list", dao.buserList());
	}
}
