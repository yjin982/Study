package pack;

import java.io.IOException;
import java.io.PrintWriter;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

/**Servlet implementation class Buy*/
@WebServlet("/Buy")
public class Buy extends HttpServlet {
	private static final long serialVersionUID = 1L;

	/**@see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)*/
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		HttpSession session = request.getSession(false);
		if(session == null) return; //결제하기니까 이미 있는 세션만 읽어서 작업하도록
		
		ArrayList<Goods> glist = (ArrayList<Goods>)session.getAttribute("list");
		if(glist == null) return;  //상품이 없는 경우 돌아가게
		
		
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<p/> ");
		
		out.println("<table border='1px' width='60%' style='text-align:center; border-collapse:collapse;'>");
		out.println("<tr><th>상품명</th><th>가격</th></tr>");
		int sum = 0;
		for (int i = 0; i < glist.size(); i++) {
			Goods goods = (Goods)glist.get(i);
			
			out.println("<tr><td>" + goods.getName() + "</td>");
			out.println("<td>" + goods.getPrice() + "</td></tr>");
			
			sum += goods.getPrice(); //총액
		}
		out.println("<tr><td colspan='2'>결제 총액 : " + sum + "</td></tr>");
		out.println("</table><p/>");
		out.println("고객님 결제 감사합니다! <br>");
		
//		session.invalidate(); //해당 고객의 모든 세션 삭제
		session.removeAttribute("list"); //해당 고객의 특정 세션만 삭제
		out.println("<a href='shop.html'>새마음으로 쇼핑 출발~</a><br>");
		
		out.println("</body></html>");
		out.close();
	}

}
