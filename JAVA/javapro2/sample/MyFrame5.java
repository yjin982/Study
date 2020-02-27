package sample;

import java.awt.Font;
import java.awt.Frame;
import java.awt.Graphics;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class MyFrame5 extends Frame{
	MyClass myClass = new MyClass();
	int x, y;		//마우스 폼 바닥을 찍었을 때의 해당 지점의 좌표
	String str[] = {"김칫국", "공깃밥", "김밥", "주먹밥", "볶음밥"};
	
	
	/*****생성자*****/
	public MyFrame5() {
		super("내부 클래스 사용"); // == setTitle(""); 
		setSize(300, 200);
		setLocation(200, 200);
		setVisible(true);
		
//	1	myClass = new MyClass();
		addWindowListener(myClass);
		addMouseListener(new OurClass()); //군더더기 최소화
		
	}
	
	
	/*****메소드*****/
	@Override
	public void paint(Graphics g) {
		int ar = (int) (Math.random() * 5); //배열이 랜덤으로 출력하게
		g.setFont(new Font("돋움", Font.BOLD, (int) (Math.random() * 50 + 8))); //폰트사이즈 랜덤 설정
		g.drawString(str[ar], x, y);
	}
	
	
	/*****내부 클래스*****/
	class MyClass extends WindowAdapter{ // 윈도우 창 닫기 위해서 내부클래스로 어답터를 받아옴
		@Override
		public void windowClosing(WindowEvent e) {
			System.exit(0);
		}
	}
	
	class OurClass extends MouseAdapter{ //마우스 이벤트 받을 마우스 어답터 내부클래스
		@Override
		public void mouseClicked(MouseEvent e) {
//	1		int m = e.getX();
//	1		int n = e.getY();
//	1		System.out.println("X : " + m + "   Y : " + n);
			setTitle("X : " + e.getX() + "   Y : " + e.getY());
			x = e.getX(); // MyFrame5의 멤버변수에 마우스 좌표값을 넘겨줌
			y = e.getY();
//	2		paint(getGraphics()); // refresh 해주지 않음
			repaint(); // refresh O
		}
	}
	
	
	
	/*****메인*****/
	public static void main(String[] args) {
		new MyFrame5();
	}
}
