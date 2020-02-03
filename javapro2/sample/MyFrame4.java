package sample;

import java.awt.Frame;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

/**리스너를 implements할 경우 필요없는 메소드까지 오버라이드 해야하는 경우가 생김 -> 인터페이스를 추상클래스로 만든 Adapter가 존재
 * but extends로 상속을 받기 때문에 하나만 가능한 단점 -> 내부 클래스 사용**/
public class MyFrame4 extends WindowAdapter{
	private Frame frame = new Frame("Adapter를 사용");
	
	//생성자
	public MyFrame4() {
		frame.setSize(300, 200);
		frame.setLocation(200, 200);
		frame.setVisible(true);
		
		frame.addWindowListener(this); //리스너 달아주기
	}
	
	//메소드
	@Override
	public void windowClosing(WindowEvent e) {
		System.exit(0);
	}
	
	/**메인**/
	public static void main(String[] args) {
		new MyFrame4();
	}
}
