package sample;

import java.awt.Frame;
import java.awt.event.WindowEvent;
import java.awt.event.WindowListener;

public class MyFrame3 extends Frame implements WindowListener{
	//생성자
	public MyFrame3() {
		super("인터페이스 사용");
		
		setSize(300, 200);
		setLocation(200, 200);
		setVisible(true);
		
		//이벤트 리스너를 해당 오브젝트(MyFrame3)에 장착
		addWindowListener(this);
	}
	
	//메소드
	@Override
	public void windowOpened(WindowEvent e) {} 
	@Override
	public void windowActivated(WindowEvent e) {} //액티브 Window 가 되었을 때
	@Override 
	public void windowClosed(WindowEvent e) {} // 윈도우가 클로즈 되었을 때
	@Override
	public void windowClosing(WindowEvent e) { // 윈도우를 닫으려고 했을 때
//		this.setTitle("안녕 반가워");
		System.exit(0);
	}
	@Override
	public void windowDeactivated(WindowEvent e) {} //액티브 Window 가 아니게 되었을 때
	@Override
	public void windowIconified(WindowEvent e) { //Window 가 최소화 되었을 때
		System.out.println("자바 만세");
	}
	@Override
	public void windowDeiconified(WindowEvent e) { //Window 가 최소화에서 돌아왔을 때
		System.out.println("오늘 불금 만세");
	}

	
	/**메인**/
	public static void main(String[] args) {
		new MyFrame3();
	}
}
