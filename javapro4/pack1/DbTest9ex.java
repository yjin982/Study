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
import javax.swing.table.DefaultTableModel;

public class DbTest9ex extends JFrame implements ActionListener{
	String [][] datas = new String[0][6];
	String [] title = {"사번", "이름", "성별", "연봉", "세금", "실수령액"};
	double tax, silpay;
	DefaultTableModel model;
	JTable table = new JTable();
	JButton btnPrint = new JButton("출력");
	JButton btnExit = new JButton("종료");
	
		
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	
	public DbTest9ex() {
		super("연봉 출력");
		
		layInit();
		accDb();
		
		DbTest9exlogin login = new DbTest9exlogin(this);
		
		setBounds(600, 100, 500, 500);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	
	private void login() {
		try {
			String sql = "select jikwon_no, jikwon_name from jikwon where jikwon_no=? and jikwon_name=?";
			
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();

			while(rs.next()) {
				
			}
			
		}catch(Exception e) {
			System.out.println("Close err\t" + e.getMessage());
		} 
	}
	public static boolean login(String no, String name) {
		//여기서 db따로 sql 작성해서 확인?
		if(no.equals("1") && name.equals("홍길동")){
			return true;
		}else {
			return false;
		}
		
	}

	private void layInit() {
		model = new DefaultTableModel(datas, title);
		table = new JTable(model);
		JScrollPane scrollpane = new JScrollPane(table);
		
		JPanel panel = new JPanel();
		panel.add(btnPrint);
		panel.add(btnExit);
		
		add("North", panel);
		add("Center", scrollpane);		
		
		btnPrint.addActionListener(this);
		btnExit.addActionListener(this);
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");

		} catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
		}
	}
	private void print() {
		try {
			String sql = "select jikwon_no, jikwon_name, jikwon_gen, jikwon_pay from jikwon";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();

			while(rs.next()) {
				calPay(rs.getDouble(4)*10000);
				String jikNo = rs.getString(1);
				String jikName = rs.getString(2);
				String jikGen = rs.getString(3);
				int jikPay = rs.getInt(4)*10000;
				
				String []imsi = {jikNo, jikName, jikGen, String.format("%,10d", jikPay), String.format("%,.0f", tax), String.format("%,.0f", silpay)};
				model.addRow(imsi);
			}
			
		}catch(Exception e) {
			System.out.println("Close err\t" + e.getMessage());
		} 
	}
	private void calPay(double pay) {
		if(pay >= 50000000) {
			tax = Math.round(pay*0.03);
			silpay = Math.round(pay - tax);
		}else {
			tax = Math.round(pay*0.03);
			silpay = Math.round(pay - tax);
		}
		//System.out.println((pay*0.03)+" " +(pay - (pay*0.03)));
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == btnPrint) {
			print();
			
		}else if(e.getSource() == btnExit) {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();
			} catch (Exception e2) {
				System.out.println("Close err\t" + e2.getMessage());
			}
			System.exit(0);
		}
		
	}
	
	public static void main(String[] args) {
		new DbTest9ex();
	}
}
