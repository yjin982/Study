package pack.controller;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;

import pack.model.HelloModel;

/**어제까지 하던 방식
public class HelloController implements Controller{
	@Override
	public ModelAndView handleRequest(HttpServletRequest request, HttpServletResponse response) throws Exception {
		return null;
	}
}
**/

public class HelloController extends AbstractController{
	private HelloModel helloModel; //모델 영역의 클래스와 통신하기 위함
	
	public void setHelloModel(HelloModel helloModel) {
		this.helloModel = helloModel;
	}
	
	@Override
	protected ModelAndView handleRequestInternal(HttpServletRequest request, HttpServletResponse response) throws Exception {
		String result = helloModel.getGreeting();
		
		ModelAndView modelAndView = new ModelAndView();
		modelAndView.setViewName("hello");  //forwarding (기본값)
		modelAndView.addObject("result", result);
//		request.setAttribute("result", result);
		
		
//		modelAndView.setViewName("redirect:/views/hello.jsp?result="+result); //리다이렉트 방식

		return modelAndView;
	}
}