package pack1;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JTextField;

/*정렬 연습(숫자는 10개 이하)
 * 대상 : 
 * 결과 : 
 * 버튼1선택 버튼2버블 버튼3지우기
 * */

public class SortExam extends JFrame implements ActionListener{
	private JPanel pn1 = new JPanel();
	private JPanel pn2 = new JPanel();
	private JPanel pn3 = new JPanel();
	JLabel lblData, lblResult, lblTitle;
	JButton btnSel, btnBub, btnClear;
	JTextField txtData, txtResult;
	
	
	public SortExam() {
		setTitle("정렬");
		initLayout();
		
		setBounds(300, 300, 400, 200);
		setResizable(false);
		setVisible(true);
		
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	public void initLayout() {
		lblTitle = new JLabel("정렬 연습");
		lblData = new JLabel("대상");
		lblResult = new JLabel("결과");
		btnSel = new JButton("Selection");
		btnBub = new JButton("Bubble");
		btnClear = new JButton("Clear");
		txtData = new JTextField("", 32);
		txtResult = new JTextField("",32);
		txtResult.setEditable(false);
		
		pn1.add(lblTitle);
		pn2.add(lblData);
		pn2.add(txtData);
		pn2.add(lblResult);
		pn2.add(txtResult);
		pn3.add(btnSel);
		pn3.add(btnBub);
		pn3.add("South",btnClear);
		
		add("North", pn1);
		add("Center", pn2);
		add("South",pn3);
		
		btnSel.addActionListener(this);
		btnBub.addActionListener(this);
		btnClear.addActionListener(this);
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		String input = "", re = "";
		int temp;
		
		input = txtData.getText();
		String str[] = input.split(" "); //문자열 받아와서 자르기
		int sort[] = new int[str.length];
		for (int i = 0; i < str.length; i++) {
			sort[i] = Integer.parseInt(str[i]);
		}//숫자로 변환
		
		
		if(e.getSource() == btnSel) {////////// selection
			
			for (int i = 0; i < sort.length-1; i++) {
				for (int j = i+1; j < sort.length; j++) {
					if(sort[i] > sort[j]) {
						temp = sort[i];
						sort[i] = sort[j];
						sort[j] = temp;
					}
				}
			}
			for (int i = 0; i < sort.length; i++) {
				re = re + (Integer.toString(sort[i]) + " ");
			}
			txtResult.setText(re);
			
		}else if(e.getSource() == btnBub) {////////// Bubble
			
			for (int i = 0; i < sort.length-1; i++) {
				for (int j = 0; j < sort.length-i-1; j++) {
					if(sort[j] > sort[j+1]) {
						temp = sort[j];
						sort[j] = sort[j+1];
						sort[j+1] = temp;
					}
				}
			}
			for (int i = 0; i < sort.length; i++) {
				re = re + (Integer.toString(sort[i]) + " ");
			}
			txtResult.setText(re);
			
		}else if(e.getSource() == btnClear) {
			txtData.setText("");
			txtResult.setText("");
		}
	}
	
	
	
	public static void main(String[] args) {
		new SortExam();
	}
}

/* 
String ss = "1 2 3 4 5";
String ar[] = ss.split(" ");
for (int i = 0; i < ar.length; i++) {
	System.out.println(ar[i]);
}
*/