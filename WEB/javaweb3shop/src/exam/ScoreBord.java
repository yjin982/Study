package exam;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**Servlet implementation class ScoreBord*/
@WebServlet("/ScoreBord")
public class ScoreBord extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**@see HttpServlet#service(HttpServletRequest request, HttpServletResponse response)*/
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		
		int num = Integer.parseInt(request.getParameter("num"));
		String name = request.getParameter("name");
		int kor = Integer.parseInt(request.getParameter("kor"));
		int eng = Integer.parseInt(request.getParameter("eng"));
		
		HttpSession session = request.getSession(true);
		
		ArrayList<Score> slist = (ArrayList<Score>)session.getAttribute("list");
		if(slist == null) slist = new ArrayList<Score>();
		
		for (int i = 0; i < slist.size(); i++) {
			Score check = (Score)slist.get(i);
			if(check.getNum() == num) {
				response.sendRedirect("exam/exam.html");
				return;
			}
		}
		
		Score sc = new Score();
		sc.setNum(num);
		sc.setName(name);
		sc.setKor(kor);
		sc.setEng(eng);
		slist.add(sc);	
		session.setAttribute("list", slist);
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<h2>세션 처리 결과</h2>");
		out.println("학생들 성적표<p/>");
		out.println("<table border='1' width='50%' style='border-collapse:collapse; text-align:center;'>");
		out.println("<tr><th>번호</th><th>이름</th><th>국어</th><th>영어</th><th>총점</th></tr>");
		
		int cnt=0;
		for (int i = 0; i < slist.size(); i++) {
			Score scGet = (Score)slist.get(i);
			out.println("<tr>");
			out.println("<td>" + scGet.getNum() + "</td>");
			out.println("<td>" + scGet.getName() + "</td>");
			out.println("<td>" + scGet.getKor() + "</td>");
			out.println("<td>" + scGet.getEng() + "</td>");
			out.println("<td>" + (scGet.getKor()+scGet.getEng()) + "</td>");
			out.println("</td></tr>");
			cnt++;
		}
		out.println("</table><p/>");
		out.println("인원수 : " + cnt + "명<br>");
		out.println("<input type='button' value='새로입력' onclick='history.back()'>&nbsp;");
		out.println("<input type='submit' value='세션삭제' onclick=\"location.href='SessionDelete'\"");
		out.println("</body></html>");
		out.close();
	}
}
