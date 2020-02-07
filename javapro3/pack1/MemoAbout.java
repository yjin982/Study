package pack1;

import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class MemoAbout extends JDialog implements ActionListener{
	/**멤버 변수**/
	
	/**생성자**/
	public MemoAbout(JFrame frame) { //JDialog의 부모
		/*
		super(frame);
		setTitle("메모장 정보"); //true : 모달, false: 모달x
		setModal(true);
		*/
		super(frame, "메모장 정보", true);
		
		JLabel label = new JLabel("미니 메모장 version 0.9");
		JButton btn = new JButton("확인");
		btn.addActionListener(this);
		add("Center", label);
		add("South", btn);
		
		setBackground(Color.DARK_GRAY);
		setBounds(350, 350, 200, 200);
		setVisible(true);
	}
		
	/**메소드**/
	@Override
	public void actionPerformed(ActionEvent e) {
		dispose(); // JDialog의 닫기
	}
}
