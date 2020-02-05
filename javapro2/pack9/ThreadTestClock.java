package pack9;

import java.awt.Button;
import java.awt.Font;
import java.awt.Frame;
import java.awt.Label;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Calendar;

public class ThreadTestClock extends Frame implements ActionListener, Runnable {
	private Label lblMessage;
	private Boolean flag = false;
	private Thread thread;
	
	/**생성자**/
	public ThreadTestClock() {
		lblMessage = new Label("Display Date & Time", Label.CENTER); // 프레임 내의 레이블의 센터
		add("Center", lblMessage); // 프레임의 센터 (창 가운데에 label 표시)
		lblMessage.setFont(new Font("Comic Sans MS", Font.BOLD, 24));
		
		Button button = new Button("click");
		add("South", button);
		button.addActionListener(this);
				
		setTitle("스레드 연습");
//		setLocation(300,400); 		setSize(300,300);
		setBounds(300, 400, 300, 300); // setLocation + setSize
		setVisible(true);
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				flag = true; // 창이 종료될 때 스레드도 종료 되도록
				System.exit(0);
			}
		});
		
		thread = new Thread(this);
		
	}
	
	
	/**메소드**/
	@Override
	public void actionPerformed(ActionEvent e) {
//		thread.start(); // 버튼 클릭 할 때마다 스레드가 생성됨
		if(thread.isAlive()) return; // 스레드가 있는지부터 체크
		thread.start();
	}
	
	private void calShow() { // 날짜 계산
		Calendar calendar = Calendar.getInstance();
		int y = calendar.get(Calendar.YEAR);
		int m = calendar.get(Calendar.MONTH) + 1;
		int d = calendar.get(Calendar.DATE);
		int h = calendar.get(Calendar.HOUR);
		int mi = calendar.get(Calendar.MINUTE);
		int s = calendar.get(Calendar.SECOND);
		
		lblMessage.setText(y +"." + m + "." + d + "  " + h + ":" + mi + ":" + s);
	}	
	// 시계가 매초 자동으로 업데이트 되도록 스레드를 생성
	@Override
	public void run() {
		while(true) {
			if(flag == true) break; // flag로 스레드가 종료되지 않고 계속 실행하지 않도록(무한루프에 빠지지 않도록) 설정
			calShow();
			try {
				Thread.sleep(1000);
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
	}
	
	
	/**=====MAIN=====**/
	public static void main(String[] args) {
		new ThreadTestClock();
	}
}
