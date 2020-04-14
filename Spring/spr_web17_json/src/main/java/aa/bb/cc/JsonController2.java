package aa.bb.cc;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("list2")
public class JsonController2 {
	
	@RequestMapping(method = RequestMethod.GET)
	@ResponseBody
	public Map getJsons() {
		List<Map<String, String>> dataList = new ArrayList<Map<String,String>>();
		Map<String, String> data = null;
		
		data = new HashMap<String, String>();
		data.put("name", "길동");
		data.put("age", "16");
		dataList.add(data);
		
		data = new HashMap<String, String>();
		data.put("name", "tom");
		data.put("age", "24");
		dataList.add(data);
		
		data = new HashMap<String, String>();
		data.put("name", "alice");
		data.put("age", "30");
		dataList.add(data);
		
		//return data;
		Map<String, Object> datas = new HashMap<String, Object>();
		datas.put("datas", dataList);
		return datas;
	}
}
