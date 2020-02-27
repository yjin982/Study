package sample;

import java.awt.Color;
import java.awt.Frame;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class MyFrame3 extends Frame implements WindowListener,MouseListener{
	//생성자
	public MyFrame3() {
		super("인터페이스 사용");
		
		setSize(300, 200);
		setLocation(200, 200);
		setVisible(true);
		
		//이벤트 리스너를 해당 오브젝트(MyFrame3)에 장착
		addWindowListener(this);
		addMouseListener(this);
	}
	
	//메소드 : 창 이벤트
	@Override
	public void windowOpened(WindowEvent e) {} 
	public void windowActivated(WindowEvent e) {} //액티브 Window 가 되었을 때
	public void windowClosed(WindowEvent e) {} // 윈도우가 클로즈 되었을 때
	public void windowClosing(WindowEvent e) { // 윈도우를 닫으려고 했을 때
//		this.setTitle("안녕 반가워");
		System.exit(0);
	}
	public void windowDeactivated(WindowEvent e) {} //액티브 Window 가 아니게 되었을 때
	public void windowIconified(WindowEvent e) { //Window 가 최소화 되었을 때
		System.out.println("자바 만세");
	}
	public void windowDeiconified(WindowEvent e) { //Window 가 최소화에서 돌아왔을 때
		System.out.println("오늘 불금 만세");
	}
	//마우스 이벤트
	int aa = 0;
	@Override
	public void mouseClicked(MouseEvent e) {
		aa++;
		System.out.println("aa : " + aa);
		//setBackground(new Color (255,255,0)); //백그라운드 (new 컬러) 변경
		//System.out.println((int)(Math.random()*255)); 255까지 난수발생
		int r = (int)(Math.random()*255);
		int g = (int)(Math.random()*255);
		int b = (int)(Math.random()*255);
		setBackground(new Color (r,g,b));
	}
	public void mouseEntered(MouseEvent e) {	}
	public void mouseExited(MouseEvent e) {}
	public void mousePressed(MouseEvent e) {}
	public void mouseReleased(MouseEvent e) {}

	
	/**메인**/
	public static void main(String[] args) {
		new MyFrame3();
	}
}
