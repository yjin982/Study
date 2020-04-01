package pack;

import java.io.IOException;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet({"/hobby.do", "/kbs.do", "*.nice", "*.kor"}) //배열형태로 {}, 여러가지 가능
public class HobbyController extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		//컨트롤러
		String hobby = request.getParameter("hobby");
		
		HobbyModel hobbyModel = HobbyModel.getInstance(); //모델과 연결(싱글톤으로)
		ArrayList<String> list = hobbyModel.getHobby(hobby);
		
		//뷰로 출력
		request.setAttribute("datas", list);
		String viewName = "hobby.jsp"; //꼭 web-inf 아래일 필요는 없으나 스프링에서는 거기를 이용
		request.getRequestDispatcher(viewName).forward(request, response);
	}

}
