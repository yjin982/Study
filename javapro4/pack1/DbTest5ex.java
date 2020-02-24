package pack1;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class DbTest5ex extends JFrame implements ActionListener{
	JButton btnFirst = new JButton("|<<");
	JButton btnPre = new JButton("<");
	JButton btnNext = new JButton(">");
	JButton btnLast = new JButton(">>|");
	JTextArea txtResult = new JTextArea(10, 20);
	JLabel lblNo = new JLabel("");
	JLabel lblName = new JLabel("");
	JLabel lblBuser = new JLabel("");
	JLabel lblBuserTel = new JLabel("");
	JLabel lblResult= new JLabel("고객번호     고객명     고객전화");
	
	String sql1 = "";
	String sql2 = "";
	String jikwonNo = "";
	Connection conn;
	Statement stmt;
	ResultSet rs1,rs2;
	
	public DbTest5ex() {
		layInit();
		accDb();
		
		setTitle("고객 자료 출력");
		setBounds(600, 100, 600, 600);
		setVisible(true);
		addWindowListener(new WindowAdapter() { //프로그램 종료하면서 db 연결 종료하도록
			@Override
			public void windowClosing(WindowEvent e) {
				try {
					if(rs1 != null) rs1.close();
					if(rs2 != null) rs2.close();
					if(stmt != null) stmt.close();
					if(conn != null) conn.close();
				} catch (Exception e2) {
					System.out.println("DB Access Close err\t" + e2.getMessage());
				}
				System.exit(0); //프로그래머 의도에 의해 정상 종료 0, 뜻하지않은 의도로 비정상 종료 1
			}
		});
	}
	
	private void layInit() {
		JPanel p1 = new JPanel();
		JPanel panel1 = new JPanel();
		panel1.add(new JLabel("사번:"));
		panel1.add(lblNo);
		panel1.add(new JLabel("이름:"));
		panel1.add(lblName);
		panel1.add(new JLabel("부서명:"));
		panel1.add(lblBuser);
		panel1.add(new JLabel("부서전화:"));
		panel1.add(lblBuserTel);
		p1.add("North",panel1);
		

		
		JPanel panel2 = new JPanel();
		panel2.add(btnFirst);
		panel2.add(btnPre);
		panel2.add(btnNext);
		panel2.add(btnLast);
		p1.add("Center",panel2);
		add("North", p1);
		
		
		
		JPanel p2 = new JPanel();
		txtResult.setEditable(false);
		JScrollPane pan = new JScrollPane(txtResult);
		
		/*JPanel panel3 = new JPanel();
		panel3.add(lblResult);*/
		p2.add("North", lblResult);
		p2.add("Center", pan);
		add("Center",p2);
		
		btnFirst.addActionListener(this);
		btnPre.addActionListener(this);
		btnNext.addActionListener(this);
		btnLast.addActionListener(this);
		
//		JPanel panel3 = new JPanel();
//		panel3.add(txtResult);
//		add("South", panel3);
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			
			stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE,ResultSet.CONCUR_READ_ONLY);
			sql1 = "select jikwon_no, jikwon_name,buser_name,buser_tel from jikwon left outer join buser on buser_num=buser_no";
			rs1 = stmt.executeQuery(sql1);
			rs1.next();
			
			jikwonNo = rs1.getString("jikwon_no");
			System.out.println(rs1.getString("jikwon_no") + rs1.getString("jikwon_name"));
			displayData1();
			displayData2();
			

		}catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
		}
	}
	private void displayData1() {
		try {
			lblNo.setText(rs1.getString("jikwon_no") + "     ");
			lblName.setText(rs1.getString("jikwon_name") + "     ");
			lblBuser.setText(rs1.getString("buser_name") + "     ");
			lblBuserTel.setText(rs1.getString("buser_tel") + "     ");

		}catch (Exception e) {
			//JOptionPane.showMessageDialog(this, "자료의 처음 또는 마지막입니다.");
			System.out.println("Display Data1 err\t" + e.getMessage());
		}
	}
	private void displayData2() {
		String ss = "";
		int count = 0;
		try {
			sql2 = "select gogek_no, gogek_name, gogek_tel,gogek_damsano from gogek where gogek_damsano="+jikwonNo;
			rs2 = stmt.executeQuery(sql2);
			
			while(rs2.next()) {
				if(jikwonNo.equals(rs2.getString("gogek_damsano"))) {
					ss += rs2.getString(1) + "\t" + rs2.getString(2) + "\t" + rs2.getString(3) + "\n";
					count ++;
				}else {
					txtResult.setText("자료가 없습니다.");
				}
			}
			txtResult.setText(ss);
			txtResult.append("\n" + count + "명");
		}catch (Exception e) {
			//JOptionPane.showMessageDialog(this, "자료의 처음 또는 마지막입니다.");
			System.out.println("Display Data2 err\t" + e.getMessage());
		}
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			if(e.getSource() == btnFirst) {
				rs1.first();
				jikwonNo = rs1.getString("jikwon_no");
			}else if(e.getSource() == btnPre) {
				rs1.previous();
				jikwonNo = rs1.getString("jikwon_no");
			}else if(e.getSource() == btnNext) {
				rs1.next();
				jikwonNo = rs1.getString("jikwon_no");
			}else if(e.getSource() == btnLast) {
				rs1.last();
				jikwonNo = rs1.getString("jikwon_no");
			}
			
			displayData1();
			displayData2();
			
			
		} catch (SQLException e1) {
			System.out.println("actionPerformed err\t" + e1.getMessage());
		}
	}
	
	
	
	public static void main(String[] args) {
		new DbTest5ex();
	}
}
