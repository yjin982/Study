package pack1;

import java.awt.BorderLayout;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;

import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;

/***** Swing 연습 *****/
public class SwingTest extends JFrame implements ActionListener{
	/**멤버 변수**/
	JLabel lblShow;
	int count = 0;
	
	/**생성자**/
	public SwingTest() {
		setTitle("스윙 연습");
		
		// 화면 디자인
		JPanel panel = new JPanel();
		panel.setLayout(new GridLayout(2,1));
		add(panel, BorderLayout.CENTER); // == add("Center", panel);
		panel.setBorder(BorderFactory.createEmptyBorder(30,30,10,30)); // top, left, bottom, right 	// ~~Factory는 스스로 new
		
		JButton btn = new JButton("클릭");
		btn.addActionListener(this);
		//// 0행
		panel.add(btn);
		//// 1행
		lblShow = new JLabel("버튼 클릭 수: 0");
		panel.add(lblShow);
		
		setBounds(300, 300, 400, 400);
		setVisible(true);
		/*awt에서의 프레임 종료
		 * addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		}); */
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //스윙에서 프레임 종료
	}
	
	
	/**메소드**/
	@Override
	public void actionPerformed(ActionEvent e) {
		count++;
		lblShow.setText("버튼 클릭 수 : " + count);
	}
	
	
	/**=== MAIN ===**/
	public static void main(String[] args) {
		new SwingTest();
	}
}
