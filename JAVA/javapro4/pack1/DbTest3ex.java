package pack1;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.swing.ButtonGroup;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JRadioButton;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class DbTest3ex extends JFrame implements ActionListener{
	JLabel label = new JLabel("직급 : ");
	JButton btnOk = new JButton("확인");
	JRadioButton rdoAsc = new JRadioButton("오름");
	JRadioButton rdoDesc = new JRadioButton("내림");
	ButtonGroup bg = new ButtonGroup();
	JTextField txtJik = new JTextField("", 10);
	JTextArea txtResult = new JTextArea();
	String sql = "";
	
	Connection conn;
	Statement stmt;
	ResultSet rs;

	
	public DbTest3ex() {
		super("직원 자료 출력");
		
		setLayout();
		setDbAccess();
		
		setBounds(750, 100, 400, 600);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	private void setLayout() {
		JPanel panel = new JPanel();
		bg.add(rdoDesc);
		bg.add(rdoAsc);
		panel.add(label);
		panel.add(txtJik);
		panel.add(btnOk);
		panel.add(rdoAsc);
		panel.add(rdoDesc);
		
		rdoAsc.setSelected(true);
		rdoDesc.setSelected(false);
		
		txtResult.setEditable(false);
		JScrollPane pane = new JScrollPane(txtResult);
		
		add("North", panel);
		add("Center", pane);
		
		btnOk.addActionListener(this);
		rdoAsc.addActionListener(this);
		rdoDesc.addActionListener(this);
	}
	private void setDbAccess() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			
		} catch (Exception e) {
			System.out.println("access err\t" + e.getMessage() );
		}
		
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			stmt = conn.createStatement();
			
			sql = "select jikwon_no, jikwon_name, jikwon_jik, jikwon_gen, buser_name, jikwon_pay from jikwon left outer join buser on buser_num=buser_no";
			
			String search = txtJik.getText();
			if(search.equals("사원") || search.equals("대리") ||search.equals("과장") || search.equals("부장") || search.equals("이사") ) { //직급 입력시
				sql += " where jikwon_jik='" + search + "'";
			}else if(search.isEmpty()){ //직급 입력 없을시
				
			}else {
				txtResult.setText("올바른 값을 입력하세요.");
				txtJik.setText("");
				txtJik.requestFocus();
				return;
			}
			
			if(rdoAsc.isSelected()){
				sql += " order by jikwon_no asc";
			}else if(rdoDesc.isSelected()) {
				sql += " order by jikwon_no desc";
			}
			
			rs = stmt.executeQuery(sql);
			int count = 0;
			double pay = 0;
			
			txtResult.setText("사번\t직원명\t직급\t성별\t부서명\n―――――――――――――――――――――――――――――――\n");
			while(rs.next()) {
				String s = rs.getString("jikwon_no") + "\t" + rs.getString("jikwon_name") + "\t" + rs.getString("jikwon_jik") + "\t"  
						 + rs.getString("jikwon_gen") + "\t" + rs.getString("buser_name") + "\t"  + "\n";
				
				txtResult.append(s);
				count++;
				pay += rs.getDouble("jikwon_pay");
			}
			
			txtResult.append("\n인원수 : " + count + "명\t 연봉평균 : " + Math.round(pay/count));
			txtJik.requestFocus();
					
		}catch (Exception e1) {
			System.out.println("DB err\t" + e1.getMessage());
		}finally {
			try {
				rs.close();
				stmt.close();
				conn.close();
			}catch (Exception e2) {
				System.out.println("close err\t" + e2.getMessage());
			}
		}
	}
	
	public static void main(String[] args) {
		new DbTest3ex();
	}
}
