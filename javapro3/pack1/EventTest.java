package pack1;

import java.awt.Button;
import java.awt.Frame;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

public class EventTest extends Frame implements ActionListener {
	/**멤버 변수**/
	private Button btn1 = new Button("Button1");
	private Button btn2 = new Button("Button2");
	private Button btn3 = new Button("Button3");
	private Button btn4 = new Button("Button4");
	private Button btn5 = new Button("Button5");
	
	
	/**생성자**/
	public EventTest() {
		super("이벤트 처리 연습");
		addLayout();
		setBounds(300, 300, 400, 400);
		setVisible(true);
		
		// 윈도우 종료 이벤트 : 내부 익명 클래스 사용
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
	}
	
	
	/**메소드**/
	private void addLayout() {
		add("East", btn1);
		add("West", btn2);
		add("South", btn3);
		add("North", btn4);
		add("Center", btn5);
		btn1.addActionListener(this); // 현재 클래스
		btn2.addActionListener(this);
		btn3.addActionListener(new MyEvent()); // 내부 클래스
		btn4.addMouseListener(new YourEvent());
		btn5.addMouseListener(new MouseAdapter() { // 윈도우 종료 이벤트 : 내부 익명 클래스 사용
			@Override
			public void mousePressed(MouseEvent e) {
				System.exit(0);
			}
		});
	}
	@Override
	public void actionPerformed(ActionEvent e) {
//		System.out.println(e.getActionCommand());  	System.out.println(e.getSource());
		if(e.getSource() == btn1) {
			this.setTitle("Button1 click");
		} else if(e.getSource() == btn2){
			setTitle("Button2 click");
		}
	}
	
	
	/**내부 클래스**/
	class MyEvent implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			setTitle("3 BUTTON CLICKED ! "); // ==	EventTest.this.setTitle("3 BUTTON CLICKED ! "); 정확하게 쓰면 이렇게(다른 클래스이기 때문에)
		}
	}
	class YourEvent extends MouseAdapter{
		@Override
		public void mouseClicked(MouseEvent e) {
			setTitle("4 BUTTON CLICKED ! ");
		}
	}
	
	
	/**=== MAIN ===**/
	public static void main(String[] args) {
		new EventTest();
	}
}
