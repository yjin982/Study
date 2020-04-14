package pack.controller;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import pack.model.DataDao;
import pack.model.JikwonDto;

@Controller
public class JikwonController {
	@Autowired
	private DataDao dao;
	
	@RequestMapping("buserjikwon")
	@ResponseBody
	public Map<String, Object> buserFunc(@RequestParam("buser_no") String no){
		List<Map<String, String>> dataList = new ArrayList<Map<String,String>>();
		Map<String, String> data = null;

		List<JikwonDto> jk = dao.jikwonList(no);
		for(JikwonDto dto : jk) {
			data = new HashMap<String, String>();
			data.put("jikwon_no", dto.getJikwon_no());
			data.put("jikwon_name", dto.getJikwon_name());
			data.put("jikwon_jik", dto.getJikwon_jik());
			
			if(dao.hasGogek(dto.getJikwon_no()) > 0) {
				data.put("jikwon_go", "O");
			}else {
				data.put("jikwon_go", "X");
			}
			dataList.add(data);
		}
		
		Map<String, Object> jikwons = new HashMap<String, Object>();
		jikwons.put("j", dataList);
		return jikwons;
	}
}
