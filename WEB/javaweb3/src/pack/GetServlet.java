package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class GetServlet
 */
@WebServlet("/GetServlet")
public class GetServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8"); //한글설정, 콘솔에선 안 깨지는데 브라우저에서 깨짐
		
		String name = request.getParameter("name");
		String age = request.getParameter("age");
		String addr = request.getParameter("addr");
		String ss = calcAge(age);
		System.out.println(name + age + addr);

		PrintWriter out = response.getWriter(); //클라이언트 브라우저로 자료 전송(출력)
		out.println("<html><head><title>연습 GET</title></head><body>");
		out.println("<b style='color:red;'>**결과 출력**</b><br>");
		out.println("이름은 " + name + "<br>나이는 " + ss + "<br>주소는 " + addr + "<br>");
		out.println("<a href='getex.html'>자료 다시 입력</a><br>");
		// 서블릿 파일 수행 수준은 webcontent 아래에 있는 것과 같다. 그래서 getex 를 부를 때 경로가 루트인것
		// sbs/aa.html 링크 경로 참조
		out.println("</body></html>");
		out.close();
	}
	
	private String calcAge(String age) {
		int imsi = Integer.parseInt(age) / 10 * 10; //  23 / 10 => 2*10 ==> 20
		String re = "";
		
		switch (imsi) {
		case 20:
			re = "이십대";		
			break;
		case 30:
			re = "삼십대";		
			break;
		default:
			re = "기타";
			break;
		}	
		return re;
	}
}
