package aa.bb.cc;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
public class MemberController {
	
	@RequestMapping(value = "member", method = RequestMethod.GET)
	public String formBack() {
		return "myform";
	}
	
	@RequestMapping(value = "member", method = RequestMethod.POST)
	@ResponseBody //리턴 결과(자바객체)를 그대로(http 응답객체로) 클라이언트 브라우저에 뿌림
	public String submit(@RequestBody String formData) { //폼태그로 받기, (name=aa&age=12) http 요청 통째로 자바객체로 받기
		System.out.println(formData);
		return "return data : " + formData;
	}
}
