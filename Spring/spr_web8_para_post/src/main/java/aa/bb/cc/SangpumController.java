package aa.bb.cc;

import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.servlet.ModelAndView;

@Controller
public class SangpumController {
	@Autowired
	private SangpumModel sangpumModel;
	
	@RequestMapping(value = "sangpum", method = RequestMethod.POST)
	/**public ModelAndView submit(SangpumBean bean) {**/
	public ModelAndView submit(@ModelAttribute("my") SangpumBean bean) {
		ModelAndView modelAndView = new ModelAndView();
		
		modelAndView.setViewName("result");
		modelAndView.addObject("data", sangpumModel.computeData(bean));
		
		return modelAndView;
	}
	
	@ModelAttribute("myList") //뷰에 직접 전달, request.setAttribute()로 전달한것같음
	public List<String> aaa(){
		List<String> list = new ArrayList<String>();
		list.add("홍길동");
		list.add("만세");
		return list;
	}
}
