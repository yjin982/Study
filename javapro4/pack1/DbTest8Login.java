package pack1;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.*;

public class DbTest8Login extends JFrame implements ActionListener{
	JTextField txtNo = new JTextField("", 5);
	JTextField txtName = new JTextField("", 10);
	JButton btnLogin = new JButton("로그인");
	JTextArea txtResult = new JTextArea();
	
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	
	public DbTest8Login() {
		super("Login");
		
		layInit();
		accDb();
		
		setBounds(600, 100, 500, 500);
		setVisible(true);
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
	}
	
	private void layInit() {
		JPanel panel1 = new JPanel();
		JScrollPane spane  = new JScrollPane(txtResult);
		
		panel1.add(new JLabel("사번 : "));
		panel1.add(txtNo);
		panel1.add(new JLabel("직원명 : "));
		panel1.add(txtName);
		panel1.add(btnLogin);
		
		add("North", panel1);
		add("Center", spane);
		
		btnLogin.addActionListener(this);
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
		} 
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		if(txtNo.getText().equals(null) || txtName.getText().equals(null)) {
			JOptionPane.showMessageDialog(this, "로그인 자료 입력!");
			return;
		}
		
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			
			String sql = "select * from jikwon where jikwon_no=? and jikwon_name=?";
			pstmt = conn.prepareStatement(sql);
			
			pstmt.setString(1, txtNo.getText());
			pstmt.setString(2, txtName.getText());
			
			rs = pstmt.executeQuery();
			if(rs.next()) {
				sql = "select jikwon_no, jikwon_name, jikwon_pay, jikwon_jik from jikwon";
				pstmt = conn.prepareStatement(sql);
				rs = pstmt.executeQuery();
				
				txtResult.setText("사번\t사원명\t연봉\t직급\n");
				while(rs.next()) {
					String bun = rs.getString("jikwon_no") + "\t";
					String irum = rs.getString("jikwon_name") + "\t";
					String pay = rs.getString("jikwon_pay") + "\t";
					String jik = rs.getString("jikwon_jik") + "\n" ;
					txtResult.append(bun + irum + pay + jik);
				}
			}else {
				txtResult.setText("실패");
			}
		} catch (Exception e1) {
			System.out.println("actionPerformed err\t" + e1.getMessage());
		} finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("Close err\t" + e2.getMessage());
			}
		}
	}
	
	
	public static void main(String[] args) {
		new DbTest8Login();
	}
}
