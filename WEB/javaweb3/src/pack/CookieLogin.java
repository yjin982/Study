package pack;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLDecoder;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**Servlet implementation class CookieLogin */
@WebServlet("/CookieLogin")
public class CookieLogin extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**@see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response) */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		
		
		//쿠키 읽기
		String id = null;
		String pwd = null;
		try {
			Cookie[] cookies = request.getCookies();  //클라이언트 컴퓨터의 모든 쿠키 읽음 (단순무식)
			for (int i = 0; i < cookies.length; i++) {
				String name = cookies[i].getName();
				System.out.println("name : " + name);
				
				if(name.equals("id")) {
					id = URLDecoder.decode(cookies[i].getValue(), "utf-8");
				}
				if(name.equals("pwd")) {
					pwd = URLDecoder.decode(cookies[i].getValue(), "utf-8");
				}
			}
			
		} catch (Exception e) {
			e.printStackTrace();
		}
		
		
		if(id != null && pwd != null) {
			out.println(id + "님 쿠키를 통해 로그인 한 상태입니다");
		}else {
			//쿠키를 읽어서 없으면 로그인 화면 출력
			out.println("** 로그인 **<br>");
			out.println("<form method='post'>");
			out.println("id : <input type='text' name='id'><br>");
			out.println("pw : <input type='text' name='pwd'><br>");
			out.println("<input type='submit' value='전송'><br>");
			out.println("</form>");
		}
		
		out.println("</body></html>");
		out.close();
	}

	/**@see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response) */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String id = request.getParameter("id");
		String pwd = request.getParameter("pwd");
		System.out.println(id + pwd);
		
		response.setContentType("text/html;charset=utf-8;");
		PrintWriter out = response.getWriter();
		
		out.println("<html><body>");
		if(id.equals("aa") && pwd.equals("11")) {
			try {
				id = URLEncoder.encode(id, "utf-8"); //암호화
				pwd = URLEncoder.encode(pwd, "utf-8");
				
				Cookie idCookie = new Cookie("id", id);
				Cookie pwdCookie = new Cookie("pwd", pwd);
				
				idCookie.setMaxAge(60*60*24*365);  //쿠키가 일년간 유효
				pwdCookie.setMaxAge(60*60*24*365);
				
				response.addCookie(idCookie);  //클라이언트에 전송 후 저장
				response.addCookie(pwdCookie);
				
				
				out.println("<h3>로그인 성공으로 쿠키 생성됨</h3>");
			}catch (Exception e) {
				e.printStackTrace();
			}
		}else {
			out.println("<h3>로그인 실패!</h3>");
		}
		out.println("</body></html>");
		out.close();
	}

}
