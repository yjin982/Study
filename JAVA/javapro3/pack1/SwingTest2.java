package pack1;

import javax.swing.JFrame;

public class SwingTest2 {
	/**=== MAIN ===**/
	public static void main(String[] args) {
		JFrame frame = new JFrame("대화상자 연습");
		
		Swing2Part part = new Swing2Part(); // Jpanel
		// ... 
		
		frame.getContentPane().add(part, "Center"); // panel 을 나누어서 작업
		frame.setJMenuBar(part.mbar);     // 프레임에 메뉴를 장착
		// ... 
		
		frame.setBounds(300, 300, 400, 300);
		frame.setVisible(true);
		
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
}
