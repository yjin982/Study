package pack;

import java.io.IOException;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**Servlet implementation class J4Servlet*/
@WebServlet("/irum.go")
public class J4Servlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**@see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)*/
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		
		String data = request.getParameter("data");
		//작업 내용
		
		/***결과 확인할 때 어느거 하나는 주석처리 후 확인하기***/
		//파일 호출 방법1 : 대상은 jsp 또는 servlet : redirect - 클라이언트를 통해 서버에 있는 파일을 호출
		response.sendRedirect("j4called.jsp?data=" + data);
		//문자이기 때문에 이런식(여기서는 get 방식 String만)으로 넘기는 것이 가능, 객체는 불가능 = 리다이렉트로는 객체를 넘기지 못함
		
		//파일 호출 방법2 : 대상은 jsp 또는 servlet : forword - 서버에서 직접 서버에 있는 파일을 호출
		request.setAttribute("key", data); //key-value 형식으로 넘겨주는데 value에 문자열뿐만이 아니라 자바의 모든 객체 형태 가능
		/**RequestDispatcher dispatcher = request.getRequestDispatcher("j4called.jsp");
		//dispatcher.forward(request, response); //jsp의 service 메소드를 부르기 때문에 request와 response를 매개변수로 넘겨줘야함, 여기 request에 윗줄에서 setAttribute한 값이 저장되어 있다*/
		request.getRequestDispatcher("j4called.jsp").forward(request, response);

	}

}
