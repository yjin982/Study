package sample;

import java.awt.Frame;

public class MyFrame2 extends Frame{//클래스 상속 연습
	//생성자
	public MyFrame2() {
		super("상속 연습");
		displayWindow();
	}

	//메소드
	void displayWindow() {
//		super.setSize(500, 300); //super나
//		this.setSize(500, 300);  //this를 쓰면 오버라이딩 된 것처럼 오해할 수도 있다
		setSize(500, 300);
		setLocation(200, 150);
		setVisible(true);
	}
	
	/**메인**/
	public static void main(String[] args) {
		new MyFrame2();
	}

}
