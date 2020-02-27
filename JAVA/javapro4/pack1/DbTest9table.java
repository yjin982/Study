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

public class DbTest9table extends JFrame{
	String [][] datas = new String[0][4];
	String [] title = {"코드", "상품명", "수량", "단가"};
	DefaultTableModel model;
	JTable table = new JTable();
	JLabel lblCount = new JLabel("건수 : ");
		
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	
	public DbTest9table() {
		super("테이블 연습");
		
		layInit();
		accDb();
		
		setBounds(600, 100, 500, 500);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	private void layInit() {
		model = new DefaultTableModel(datas, title);
		table = new JTable(model);
		JScrollPane scrollpane = new JScrollPane(table);

		add("Center", scrollpane);
		add("South", lblCount);
		
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			pstmt = conn.prepareStatement("select * from sangdata");
			rs = pstmt.executeQuery();
			
			int count = 0;
			while(rs.next()) {
				String code = rs.getString("code");
				String sang = rs.getString("sang");
				String su = rs.getString("su");
				String dan = rs.getString("dan");
				
				String []imsi = {code, sang, su, dan};
				model.addRow(imsi);
				
				count++;
			}
			lblCount.setText("건수 : " + count);
		} catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
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
		new DbTest9table();
	}
}
