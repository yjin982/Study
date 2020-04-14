package pack.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import pack.model.DataDao;
import pack.model.SangpumDto;

@Controller
public class SangpumController {
	@Autowired
	private DataDao dao;
	
	@RequestMapping("sangpum")
	@ResponseBody
	public Map<String, Object> sangpumFunc() {
		List<Map<String, String>> dataList = new ArrayList<Map<String,String>>();
		Map<String, String> data = null;
		
		List<SangpumDto> sangList = dao.sangpumList(); //모델과 통신
		for(SangpumDto dto : sangList) {
			data = new HashMap<String, String>();
			data.put("code", dto.getCode());
			data.put("sang", dto.getSang());
			data.put("su", dto.getSu());
			data.put("dan", dto.getDan());
			dataList.add(data);
		}
		
		Map<String, Object> sangpums = new HashMap<String, Object>();
		sangpums.put("sangpums", dataList);
		return sangpums;
	}
}
