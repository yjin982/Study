package aa.bb.cc;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@RequestMapping("list")
public class JsonController {
	@Autowired
	private MyModel myModel;
	
	@RequestMapping(method = RequestMethod.GET)
	@ResponseBody
	public MyModel getJson(@RequestParam("name") String name) {
		myModel.setName(name);
		myModel.setSkills(new String[] {"java", "c", "python"});
		return myModel;
	}
}
