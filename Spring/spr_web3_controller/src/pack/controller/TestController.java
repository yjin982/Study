package pack.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.Controller;

public class TestController implements Controller{
	
	@Override
	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
		// 컨트롤러 영역에 있는 클래스 : 모델(DB쪽)에 있는 특정 클래스와 커뮤니케이션 함
		System.out.println("TestController 수행 : 모델에 다녀왔다고 가정");
		
		//return new ModelAndView("list");   //파라미터로 view 파일 이름을 줌, 경로와 확장자는 다른 곳에서 prefix suffix로 넣어줌
		
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("list");
		modelAndView.addObject("key", "모델에서 얻은 스프링 만세");
		return modelAndView;
	}
}
