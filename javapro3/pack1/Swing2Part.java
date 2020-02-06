package pack1;

import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

public class Swing2Part extends JPanel implements ActionListener{
	/**멤버 변수**/
	JButton btnR, btnG, btnB;
	JMenuBar mbar;
	JMenuItem mnuMes, mnuOk, mnuInput;
	JTextArea txtArea = new JTextArea("", 10,50); // 스크롤바 없음
	
	/**생성자**/
	public Swing2Part() {
		setLayout(new BorderLayout()); //Flow를 Border로
		
		btnR = new JButton("빨강");
		btnG = new JButton("초록");
		btnB = new JButton("파랑");
		btnR.addActionListener(this);
		btnG.addActionListener(this);
		btnB.addActionListener(this);
		
		JPanel panel = new JPanel(); //Flow
		panel.add(btnR);
		panel.add(btnG);
		panel.add(btnB);
		
		add("South", panel);
		add("Center", txtArea);
		
		menuProcess();
	}
	
	/**메소드**/
	@Override
	public void actionPerformed(ActionEvent e) {
		if		 (e.getSource() == btnR)		txtArea.setBackground(Color.RED);
		else if(e.getSource() == btnG) 		txtArea.setBackground(Color.GREEN);
		else if(e.getSource() == btnB)		txtArea.setBackground(new Color(0, 0, 255));
		else if(e.getSource() == mnuMes) {
			JOptionPane.showMessageDialog(this, "메세지", "알림", JOptionPane.INFORMATION_MESSAGE);
			System.out.println("Modal DialogBox가 닫히면 수행"); // 모달 / this 가 알림창의 부모
			
		}else if(e.getSource() == mnuOk) {
			int re = JOptionPane.showConfirmDialog(this, "골라", "확인", JOptionPane.YES_NO_CANCEL_OPTION);
			System.out.println(re);
			
			switch (re) {
			case JOptionPane.YES_OPTION: //case 0:
				txtArea.append("예 선택\n");	//txtArea.setText("예 선택"); // 덮어쓰기
				break;
			case JOptionPane.NO_OPTION:
				txtArea.append("아니오 선택\n");
				break;
			case JOptionPane.CANCEL_OPTION:
				txtArea.append("취소 선택\n");
				break;
			}
			
		}else if(e.getSource() == mnuInput) {
			String str = JOptionPane.showInputDialog(this, "자료입력");
			txtArea.append(str + "\n");
		}
		
		
	}
	private void menuProcess() {
		mbar = new JMenuBar();
		JMenu menu = new JMenu("대화상자");
		mnuMes = new JMenuItem("메시지");
		mnuOk = new JMenuItem("확인");
		mnuInput = new JMenuItem("입력");
		menu.add(mnuMes);
		menu.add(mnuOk);
		menu.add(mnuInput);
		mbar.add(menu);  // 메뉴바에 메뉴 등록
		
		// 메뉴에 리스너 등록
		mnuMes.addActionListener(this);
		mnuOk.addActionListener(this);
		mnuInput.addActionListener(this);
	}
}
