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

/**Servlet implementation class BangServlet*/
@WebServlet("/BangServlet")
public class BangServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;
	private Connection conn;
	private PreparedStatement pstmt;
	
	
	/**@see Servlet#init(ServletConfig)*/
	public void init(ServletConfig config) throws ServletException {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/mydb", "root", "123");
			pstmt = conn.prepareStatement("insert into miniguest(name, subject, content) values(?,?,?)");
		} catch (Exception e) {
			System.out.print("new init err : ");
			e.printStackTrace();
		}
	}

	/**@see Servlet#destroy()*/
	public void destroy() {
		try {
			if(pstmt != null) pstmt.close();
			if(conn != null) conn.close();
		} catch (Exception e) {
			System.out.print("new destroy err : ");
			e.printStackTrace();
		}
	}

	/**@see HttpServlet#doPost(HttpServletRequest request, HttpServletResponse response)*/
	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		request.setCharacterEncoding("utf-8");
		String name = request.getParameter("name");
		String subject = request.getParameter("subject");
		String content = request.getParameter("content");
		//System.out.println(name+subject+content);
		
		try {
			pstmt.setString(1, name);
			pstmt.setString(2, subject);
			pstmt.setString(3, content);
			int re = pstmt.executeUpdate()	;
			
//			response.sendRedirect("bang/bangmain.html");
			
			
			response.setContentType("text/html;charset=utf-8");
			PrintWriter out = response.getWriter();
			out.println("<html><body>");
			out.println("<b>" + name + "</b>님 등록 완료<br>");
			out.println("<a href='bang/bangmain.html'>새글 입력</a>&nbsp;");
			out.println("<a href='BangList'>글 내용 보기</a>&nbsp;");
			out.println("</body></html>");
			out.close();
			
		} catch (Exception e) {
			System.out.print("doPost err : ");
			e.printStackTrace();
		}
		
	}

}
