package pack1;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.*;
import javax.swing.table.DefaultTableModel;

public class DbTest11 extends JFrame implements ActionListener{
	Connection conn;
	PreparedStatement pstmt1, pstmt2, pstmt3;
	ResultSet rs1, rs2, rs3;
	String sql = "";
	
	String datas[][] = new String[0][4];
	String title[] = {"부서번호", "부서명","부서전화","부서위치"};
	String buserName;
	DefaultTableModel model;
	JTable table;
	JTextArea txtResult;
	
	
	public DbTest11() {
		super("부서명 클릭");
		
		layInit();
		setBounds(600, 100, 400, 400);
		setVisible(true);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		accDb();
		showData();
		
		table.addMouseListener(new MouseAdapter() { //테이블에 마우스리스너 장착
			@Override
			public void mouseClicked(MouseEvent e) {
				table = (JTable) e.getComponent();
				model = (DefaultTableModel) table.getModel();
//				System.out.println("행/열 번호 : " + table.getSelectedRow() + " / " + table.getSelectedColumn()); 선택된 행/열 얻기
//				System.out.println("열 이름 : " + table.getColumnName(table.getSelectedColumn())); //선택된 행열의 열 이름 얻기
//				System.out.println("선택된 칸의 값 : " + model.getValueAt(table.getSelectedRow(), table.getSelectedColumn()));  //선택된 칸의 값 얻기
//				System.out.println("선택된 칸의 부서 : " + model.getValueAt(table.getSelectedRow(), 1));
				
				buserName = (String) model.getValueAt(table.getSelectedRow(), 1);
				
				showResult();
			}
			
		});
	}
	
	
	private void layInit() {
		setLayout(new GridLayout(2,1));
		model = new DefaultTableModel(datas, title);
		table = new JTable(model);
		JScrollPane pane1 = new JScrollPane(table);
		
		txtResult = new JTextArea();
		txtResult.setEditable(false);
		JScrollPane pane2 = new JScrollPane(txtResult);
		
		add("North", pane1);
		add("South", pane2);
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
		}
	}
	private void showData() {
		sql = "select * from buser";
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			pstmt1 = conn.prepareStatement(sql);
			rs1 = pstmt1.executeQuery();
			
			while(rs1.next()) {
				String data[] = { rs1.getString(1), rs1.getString(2), rs1.getString(3), rs1.getString(4) };
				model.addRow(data);
			}
			
		} catch (Exception e1) {
			System.out.println("DB display err\t" + e1.getMessage());
		}finally {
			try {
				if(rs1 != null) rs1.close();
				if(rs2 != null) rs2.close();
				if(rs3 != null) rs3.close();
				if(pstmt1 != null) pstmt1.close();
				if(pstmt2 != null) pstmt2.close();
				if(pstmt3 != null) pstmt3.close();
				if(conn != null) conn.close();						
			}catch (Exception e2) {
				System.out.println("DB Close err\t" + e2.getMessage());
			}
		}
	}
	private void showResult() {
		txtResult.setText("");
		
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			String sql2 = "select jikwon_no, jikwon_name, jikwon_jik from jikwon "
					+ "right outer join buser on buser_num=buser_no where buser_name=?";
			pstmt2 = conn.prepareStatement(sql2);
			pstmt2.setString(1, buserName);
			rs2 = pstmt2.executeQuery();
			
			while(rs2.next()) {
				String ss = rs2.getString(1) + "\t" + rs2.getString(2) + "\t" + rs2.getString(3) + "\n";
				txtResult.append(ss);
			}
			
		} catch (Exception e) {
			System.out.println("Result display err\t" + e.getMessage());
		}finally {
			try {
				if(rs1 != null) rs1.close();
				if(rs2 != null) rs2.close();
				if(rs3 != null) rs3.close();
				if(pstmt1 != null) pstmt1.close();
				if(pstmt2 != null) pstmt2.close();
				if(pstmt3 != null) pstmt3.close();
				if(conn != null) conn.close();						
			}catch (Exception e2) {
				System.out.println("DB Close err\t" + e2.getMessage());
			}
		}
	}
	@Override
	public void actionPerformed(ActionEvent e) {
	
	}
	
	
	
	public static void main(String[] args) {
		new DbTest11();
	}
}
