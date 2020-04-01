package pack;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/GoMvc")
public class GoMvc extends HttpServlet { //controller 역할

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		
		String msg, result = "", viewName = "";
		
		try {
			msg = request.getParameter("msg");
			///////... 더 많은 요청이 있다고 가정
			
		}catch (Exception e) {
			msg = null;
		}
		
		//클라이언트의 요청을  판단해서 비즈니스 로직과 view를 판단
		if(msg == null || msg.equals("")) { 
			result = "환영합니다";  //모델에서 수행된 결과를 치환했다고 가정(==모델을 다녀왔다고)
			//모델이 제공한 view 파일명을 얻었다고 가정
			viewName = "/WEB-INF/views/gomvc1.jsp"; //클라이언트는 접근 불가능, 서버에서 서버를 부를때
		}else if(msg.equals("korea")){
			result = "대한민국";  //스트링이 아니라 컬렉션일수도, 디비에서 불러온 자료일수도 있다.
			viewName = "/WEB-INF/views/gomvc2.jsp";
		}else {
			result = msg; 
			viewName = "/WEB-INF/views/gomvc2.jsp";
		}
		
		RequestDispatcher dispatcher = request.getRequestDispatcher(viewName);
		request.setAttribute("result", result);
		dispatcher.forward(request, response);
		
	}

}
