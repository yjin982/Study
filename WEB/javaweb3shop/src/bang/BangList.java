package bang;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/**Servlet implementation class BangList*/
@WebServlet("/BangList")
public class BangList extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private Connection conn;
	private PreparedStatement pstmt;
	private ResultSet rs;

	/**@see Servlet#init(ServletConfig) */
	public void init(ServletConfig config) throws ServletException {
		
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "123");
			pstmt = conn.prepareStatement("select * from miniguest order by code desc");
		} catch (Exception e) {
			System.out.print("list init err : ");
			e.printStackTrace();
		}
	}

	/**@see Servlet#destroy()*/
	public void destroy() {
		try {
			if(pstmt != null) pstmt.close();
			if(conn != null) conn.close();
		} catch (Exception e) {
			System.out.print("list destroy err : ");
			e.printStackTrace();
		}
	}

	/**@see HttpServlet#doGet(HttpServletRequest request, HttpServletResponse response)	 */
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		response.setContentType("text/html;charset=utf-8");
		PrintWriter out = response.getWriter();
		out.println("<html><body>");
		out.println("<h2>글 내용</h2>");
		out.println("<a href='bang/bangmain.html'>글 쓰기</a><p/>");
		out.println("<table border='1px' width='80%' style='border-collapse:collapse; text-align:center;'>");
		
		try {
			rs = pstmt.executeQuery();
			while(rs.next()) {
				out.println("<tr style='background-color:#FAF4C0;'>");
				out.println("<td>코드</td><td>" + rs.getString("code") + "</td></tr>");
				
				out.println("<tr>");
				out.println("<td>작성자</td><td>" + rs.getString("name") + "</td></tr>");

				out.println("<tr>");
				out.println("<td>제목</td><td>" + rs.getString("subject") + "</td></tr>");

				out.println("<tr>");
				out.println("<td height='100'>내용</td><td>" + rs.getString("content") + "</td></tr>");

			}
		} catch (Exception e) {
			System.out.print("list doget err : ");
			e.printStackTrace();
		}
		
		out.println("</table>");
		out.println("</body></html>");
		out.close();
	}

}
