package sample;

import java.awt.Frame;

public class MyFrame1 {//클래스 포함 연습
	//멤버 변수
	private Frame fr;
	
	//생성자
	public MyFrame1() {
		fr = new Frame("포함 연습용");
		displayWindow();
	}
	
	//메소드
	public void displayWindow() {
		fr.setSize(500, 300);
		fr.setLocation(200, 150);
		fr.setVisible(true);
	}
	
	/**메인**/
	public static void main(String[] args) {
		//MyFrame1 frame1 = new MyFrame1();
		//frame1.displayWindow();
		
		new MyFrame1();
	}

}
