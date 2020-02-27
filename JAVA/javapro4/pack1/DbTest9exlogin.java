package pack1;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class DbTest9exlogin extends JDialog{
	JButton btnOk = new JButton("확인");
	JTextField txtNo = new JTextField("", 10);
	JTextField txtName = new JTextField("",10);
	int cnt = 3;
	
	public DbTest9exlogin(JFrame frame) {
		super(frame, "로그인", true);
		
		JPanel p1 = new JPanel();
		p1.add(new JLabel("사번 : "));
		p1.add(txtNo);
		p1.add(new JLabel("이름 : "));
		p1.add(txtName);
		JPanel p2 = new JPanel();
		p2.add(btnOk);
		add("Center", p1);
		add("South",p2);
		
		
		btnOk.addActionListener(new ActionListener() { //3번 한정은 ㄴㄴㄴ
			@Override
			public void actionPerformed(ActionEvent e) {
				if(DbTest9ex.login(txtNo.getText(), txtName.getText())){
					dispose();
				}else {
					txtNo.setText("");
					txtName.setText("");
					txtNo.requestFocus();
				}
			}
		});
		
		setBounds(500, 200, 200, 150);
		setVisible(true);
		
	}
}
