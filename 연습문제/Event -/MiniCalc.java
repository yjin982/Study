package pack1;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JTextField;

public class MiniCalc extends JFrame implements ActionListener{
	JLabel lblNum1, lblNum2, lblCal, lblResult, lblCalResult;
	JTextField txtNum1, txtNum2;
	JButton btnCal, btnInit, btnExit;
	ButtonGroup group = new ButtonGroup();
	JRadioButton rdoP, rdoS, rdoD, rdoM;
	
	
	public MiniCalc() {
		super("미니 계산기");
		initLayout();
		
		setBounds(300, 300, 350, 300);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	
	private void initLayout() {
		setLayout(new GridLayout(5,1));

		/// 1
		JPanel pn1 = new JPanel();
		lblNum1 = new JLabel("숫자 1 : ");
		txtNum1 = new JTextField("", 20);
		pn1.add(lblNum1);
		pn1.add(txtNum1);
		add(pn1);
		
		
		/// 2
		JPanel pn2 = new JPanel();
		lblNum2 = new JLabel("숫자 2 : ");
		txtNum2 = new JTextField("", 20);
		pn2.add(lblNum2);
		pn2.add(txtNum2);
		add(pn2);
		
		/// 3
		JPanel pn3 = new JPanel();
		lblCal = new JLabel("연산 선택 : ");
		rdoP = new JRadioButton("+", true);
		rdoS = new JRadioButton("-", false);
		rdoM = new JRadioButton("*", false);
		rdoD = new JRadioButton("/", false);
		group.add(rdoP);
		group.add(rdoS);
		group.add(rdoM);
		group.add(rdoD);
		pn3.add(lblCal);
		pn3.add(rdoP);
		pn3.add(rdoS);
		pn3.add(rdoM);
		pn3.add(rdoD);
		add(pn3);
		
		
		/// 4
		JPanel pn4 = new JPanel();
		lblResult = new JLabel("결과 : ");
		lblCalResult = new JLabel("");
		pn4.add(lblResult);
		pn4.add(lblCalResult);
		add(pn4);
		
		/// 5
		JPanel pn5 = new JPanel();
		btnCal = new JButton("계산");
		btnInit = new JButton("초기화");
		btnExit = new JButton("종료");
		btnCal.addActionListener(this);
		btnInit.addActionListener(this);
		btnExit.addActionListener(this);
		pn5.add(btnCal);
		pn5.add(btnInit);
		pn5.add(btnExit);
		add(pn5);
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		// 계산
		int x=0 ,y = 0, re = 0;
		if(e.getSource() == btnCal) {
			if(txtNum1.getText().equals("")) {
				JOptionPane.showMessageDialog(this, "숫자를 입력하세요");
				txtNum1.requestFocus();
				
			}else if(txtNum2.getText().equals("")) {
				JOptionPane.showMessageDialog(this, "숫자를 입력하세요");
				txtNum2.requestFocus();
				
			}else {
				try {// 입력값 확인
					x = Integer.parseInt(txtNum1.getText());
					y = Integer.parseInt(txtNum2.getText());
				}catch (Exception err) {
					JOptionPane.showMessageDialog(this, "숫자만 입력하세요");
					System.out.println(err.getMessage());
				}
			}
			
			// 연산 선택 확인 후 계산
			if(rdoP.isSelected()) {
				re = x + y;
				lblCalResult.setText(Integer.toString(re));
			}else if(rdoS.isSelected()) {
				re = x - y;
				lblCalResult.setText(Integer.toString(re));
			}else if(rdoM.isSelected()) {
				re = x * y;
				lblCalResult.setText(Integer.toString(re));
			}else if(rdoD.isSelected()){
				double zd = 0;
				zd = (double)x / (double)y;			
				
				if(Double.isInfinite(zd)) {
					JOptionPane.showMessageDialog(this, "0으로 나눌 수 없습니다.");
					lblCalResult.setText("");
				}
				else if(Double.isNaN(zd)) {
					JOptionPane.showMessageDialog(this, "유효하지 않는 값입니다.");
					lblCalResult.setText("");
				}else {
					zd = Math.round(zd*100)/100.0;
					lblCalResult.setText(Double.toString(zd));
				}
			}
		}
		
		// 초기화
		if(e.getSource() == btnInit) {
			txtNum1.setText(null);
			txtNum2.setText(null);
			group.clearSelection();
			rdoP.setSelected(true);
			txtNum1.requestFocus();
		}
		
		// 종료
		if(e.getSource() == btnExit) {
			int r = JOptionPane.showConfirmDialog(this, "정말로 종료하시겠습니까?", "종료", JOptionPane.YES_NO_OPTION, JOptionPane.QUESTION_MESSAGE);
			if(r == JOptionPane.YES_OPTION)  System.exit(0);
		}
	}
	
	public static void main(String[] args) {
		new MiniCalc();
	}
}
