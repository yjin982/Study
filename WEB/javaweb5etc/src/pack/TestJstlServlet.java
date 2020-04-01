package pack;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/TestJstlServlet")
public class TestJstlServlet extends HttpServlet {
	
	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		String irum = "사오정";
		request.setAttribute("man", irum);
		
		Person person = new Person();
		person.setName("한국인");
		request.setAttribute("person", person);
		
		Student student = new Student();
		student.setAge(33);
		request.setAttribute("student", student);
		
		//문자열
		String[] ani = {"말", "댕댕", "갓랑이"};
		request.setAttribute("animal", ani);
		
		String[] food = {"당근", "개밥", "동물"};
		List<Object> list = new ArrayList<Object> ();
		list.add(ani);
		list.add(food);
		request.setAttribute("list", list);
		
		request.getRequestDispatcher("test_jstl.jsp").forward(request, response);
	}

}
