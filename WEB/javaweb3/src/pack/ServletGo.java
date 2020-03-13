package pack;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletConfig;
import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

@WebServlet("/kor.mbc") //어노테이션으로 web.xml에 서블릿 등록한 효과를 줌
public class ServletGo extends HttpServlet {
	private OurClass our = null;
//	public ServletGo() {
//		System.out.println("ServletGo 생성자"); //시작하면서 생성자 먼저 실행, 1번만
//	} //그렇지만 생성자는 거의 쓰지 않음 대신 init으로 초기화

	
	/////서블릿 라이프 사이클
	public void init(ServletConfig config) throws ServletException { //초기화 담당
		System.out.println("init"); //시작하면서 생성자 다음 실행, 1번만 수행
		our = new OurClass();
	}

	public void destroy() { //마무리 담당
		System.out.println("destroy - 수행"); //서비스 종료시 1번만 수행
		our = null;
	}
	
	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("nice - doGet");	//service주석처리시 실행, get방식
		
		response.setContentType("text/html;charset=utf-8"); //한글설정
		PrintWriter out = response.getWriter(); //클라이언트 브라우저로 자료 전송(출력)
		out.println("<html><head>연습</head><body>");
		out.println("<h1>서블릿 시작</h1>");
		
		int a = 10, b = 28;
		out.println("a=" + a + " , b=" + b + "<br>");
		int tot = myCalc(a, b);
		out.println("tot=" + tot + "<br>");
		out.println("이름은 " +  our.getIrum());

		out.println("</body></html>");
		
		out.close();
		
	}
	private int myCalc(int a, int b) {
		return a+b;
	}
	
	/*
//	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		System.out.println("nice - doPost");
//		//doGet주석처리시 405에러, jsp에서는 못보는 에러, 
//	}
//	jsp 코드는 이 메소드 안에 쓴 것과 동일
//	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
//		service는 get, post방식 모두 처리
//		System.out.println("good - service"); // 모든 클라이언트 요청시 계속 수행(요청한 갯수만큼 수행)
//	}
	 */
}
