package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**
 * Servlet implementation class PostServlet
 */
@WebServlet("/PostServlet")
public class PostServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**
	 * @see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)
	 */
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8"); //한글설정
		request.setCharacterEncoding("utf-8"); //콘솔에서도 깨져서 설정, get에서는 안깨질 때도 있음
		
		String name = request.getParameter("name");
		String addr[] = request.getParameterValues("addr");
		String lan[] = request.getParameterValues("lan");
		String os = request.getParameter("os");
		String tr = request.getParameter("tr");
		String msg = request.getParameter("msg");
		System.out.println(name + addr[0] + addr[1]);
		
		PrintWriter out = response.getWriter(); //클라이언트 브라우저로 자료 전송(출력)
		out.println("<html><head><title>연습 POST</title></head><body>");
		out.println("<b style='color:blue;'>** 결과 출력 **</b><br>");
		out.println("이름은 " + name + "<br>주소는 ");
		for (int i = 0; i < addr.length; i++) {
			out.print(addr[i] + " ");
		}
		
		//체크박스
		try {
			out.print("<br>선택한 언어는 ");
			for (String la : lan) {
				out.print(la + ", ");
			}
			out.print("<br>");
		} catch (Exception e) {
			e.printStackTrace();
			out.print("<br>하나 이상의 언어를 선택해 주세요.<br>");
		}
		
		//라디오
		out.print("운영체제는 " + os + "<br>");
		
		//셀렉트
		out.print("교통 수단은 " + tr + "<br>");
		out.print("메세지 :  " + msg + "<br>");
		
		out.println("<br><a href='postex.html'>자료 다시 입력</a><br>");
		out.println("</body></html>");
		out.close();
	}

}
