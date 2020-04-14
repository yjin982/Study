package pack.aspect;

import java.io.IOException;

import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.springframework.stereotype.Component;

@Component
public class LoginClass {
	
	public boolean loginCheck(HttpServletRequest request, HttpServletResponse response) throws IOException {
		HttpSession session = request.getSession();
		
		if(session.getAttribute("name") == null) {
			response.sendRedirect("login");
			return true;
		}else {			
			return false; //로그인이 되어있음
		}
	}
}
