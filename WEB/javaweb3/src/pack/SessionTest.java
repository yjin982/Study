package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**Servlet implementation class SessionTest */
@WebServlet("/SessionTest")
public class SessionTest extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**@see HttpServlet#service(HttpServletRequest request, HttpServletResponse response) */
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession(true); // true:세션이 있으면 읽고, 없으면 생성O / false:세션이 있으면 읽고, 없으면 생성X
		session.setMaxInactiveInterval(60); //1분간 세션 유효, 기본 30분
		if(session != null) 
			session.setAttribute("name", "홍길동");   // 쿠키=String, 세션=Object 으로 처리
					
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("session id : " + session.getId() + "<br>");
		out.println("사용자명 : " + session.getAttribute("name") + "<br>");
		
		out.println("</body></html>");
		out.close();
	}

}
