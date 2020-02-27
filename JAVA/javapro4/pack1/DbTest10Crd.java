package pack1;

import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTable;
import javax.swing.JTextField;
import javax.swing.table.DefaultTableModel;

public class DbTest10Crd extends JFrame implements ActionListener{
	String [][] datas = new String[0][5];
	String [] title = {"코드", "상품명", "수량", "단가", "금액"};
	DefaultTableModel model = new DefaultTableModel(datas, title);
	JTable table = new JTable(model);
	
	JLabel lblCou = new JLabel("건수 : ");
	JButton btnInsert = new JButton("추가");
	JButton btnDelete = new JButton("삭제");
	JButton btnExit = new JButton("종료");
	
	Connection conn;
	PreparedStatement pstmt;
	ResultSet rs;
	
	
	public DbTest10Crd() {
		layInit();
		accDb();
		
		setTitle("상품처리");
		setResizable(false);
		setBounds(600, 100, 400, 400);
		setVisible(true);
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				int re = JOptionPane.showConfirmDialog(DbTest10Crd.this, "정말로 종료할까요?", "종료", JOptionPane.OK_CANCEL_OPTION);
				if (re == JOptionPane.OK_OPTION) {
					try {
						if(rs != null) rs.close();
						if(pstmt != null) pstmt.close();
						if(conn != null) conn.close();						
					}catch (Exception e1) {
						System.out.println("DB Close err\t" + e1.getMessage());
					} finally {
						System.exit(0);
					}
				} else {
					setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
				}
			}
		});
	}
	
	private void layInit() {
		JPanel panel = new JPanel();
		panel.add(btnInsert);
		panel.add(btnDelete);
		panel.add(btnExit);
		add("North", panel);
		
		//테이블 열폭 사이즈 조절
		table.getColumnModel().getColumn(0).setPreferredWidth(40);
		table.getColumnModel().getColumn(1).setPreferredWidth(150);
		//테이블 열폭 이동 크기조절 
		table.getTableHeader().setReorderingAllowed(false);//이동불가 (따로추가)
		table.getTableHeader().setResizingAllowed(false); //크기조절불가(따로추가)
		JScrollPane scrollpane = new JScrollPane(table);
		add("Center", scrollpane);
				
		add("South", lblCou);
		
		//listener
		btnInsert.addActionListener(this);
		btnDelete.addActionListener(this);
		btnExit.addActionListener(this);
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
		} catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
		}
		dispData();
	}
	private void dispData() {
		model.setNumRows(0); //테이블 초기화 후 다시 뿌리기 위해
		
		try {
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			String sql = "select * from sangdata";
			pstmt = conn.prepareStatement(sql);
			rs = pstmt.executeQuery();
			
			int count = 0;
			while(rs.next()) {
				int keum = rs.getInt("su") * rs.getInt("dan");
				String[] imsi = { 
						rs.getString("code"),
						rs.getString("sang"),
						rs.getString("su"),
						rs.getString("dan"),
						Integer.toString(keum)
				};
				model.addRow(imsi);
				count++;
			}
			lblCou.setText("건수 : " + count);

		} catch (Exception e) {
			System.out.println("DB display err\t" + e.getMessage());
		}finally {
			try {
				if(rs != null) rs.close();
				if(pstmt != null) pstmt.close();
				if(conn != null) conn.close();						
			}catch (Exception e1) {
				System.out.println("DB Close err\t" + e1.getMessage());
			}
		}
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == btnInsert) { //추가
			InsertForm insertForm = new InsertForm(this); //추가를 위한 내부 클래스
			
			dispData(); //추가 후 자료보기
		}else if(e.getSource() == btnDelete) {//삭제 번호만 물어보고 삭제하면 쉬움 
			String delNo = JOptionPane.showInputDialog(this, "삭제할 상품 코드 입력");
			if(delNo==null) return; //입력 안했으면 창 종료
			
			//삭제
			try {
				conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
				String sql = "delete from sangdata where code=?";
				pstmt = conn.prepareStatement(sql);
				pstmt.setString(1, delNo.trim());
				
				if(pstmt.executeUpdate() == 0) {
					JOptionPane.showMessageDialog(this, delNo + "번은 등록된 코드가 아닙니다");
					return;
				}
				dispData(); //삭제 후 자료보기
				/**삭제의 경우는 '정말 삭제할까요?' 라고 물어보는 것을 매우 권장. 실수로 삭제를 할 경우 돌이킬 수 없기 때문에**/
			}catch (Exception e2) {
				System.out.println("삭제 실패\t"+ e2.getMessage());
			}finally {
				try {
					if(rs != null) rs.close();
					if(pstmt != null) pstmt.close();
					if(conn != null) conn.close();						
				}catch (Exception e1) {
					System.out.println("DB Close err\t" + e1.getMessage());
				}
			}
						
		}else if(e.getSource() == btnExit) {//종료 --46라인 복사
			int re = JOptionPane.showConfirmDialog(DbTest10Crd.this, "정말로 종료할까요?", "종료", JOptionPane.OK_CANCEL_OPTION);
			if (re == JOptionPane.OK_OPTION) {
				try {
					if(rs != null) rs.close();
					if(pstmt != null) pstmt.close();
					if(conn != null) conn.close();						
				}catch (Exception e1) {
					System.out.println("DB Close err\t" + e1.getMessage());
				} finally {
					System.exit(0);
				}
			} else {
				setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
			}
		}
	}
	
	/**추가를 위한 내부 클래스**/
	class InsertForm extends JDialog implements ActionListener{
		JTextField txtSang = new JTextField("", 10);
		JTextField txtSu = new JTextField("", 10);
		JTextField txtDan = new JTextField("", 10);
		JButton btnOk = new JButton("등록");
		JButton btnCancel = new JButton("지움");
		
		public InsertForm(JFrame frame) {
			super(frame, "상품 추가"); //super(frame, "상품 추가", true);
			setModal(true);

			add("North", new JLabel("상품 자료 입력"));
			
			JPanel pn1 = new JPanel(new GridLayout(4,2));
			pn1.add(new JLabel("품명 : "));
			pn1.add(txtSang);
			pn1.add(new JLabel("수량 : "));
			pn1.add(txtSu);
			pn1.add(new JLabel("단가 : "));
			pn1.add(txtDan);
			pn1.add(btnOk);
			pn1.add(btnCancel);
			add("Center", pn1);
			
			btnOk.addActionListener(this);
			btnCancel.addActionListener(this);
			
			setBounds(700, 200, 200, 150);
			setVisible(true);
			
			addWindowListener(new WindowAdapter() {
				@Override
				public void windowClosing(WindowEvent e) {
					dispose();
				}
			});
			
		}
		@Override
		public void actionPerformed(ActionEvent e) {
			if(e.getSource() == btnOk) { 
				//상품 추가
				if(txtSang.getText().equals("")) {//입력 자료 검사
					JOptionPane.showMessageDialog(this, "상품명 입력");
					txtSang.requestFocus();
					return;
				}
				if(txtSu.getText().equals("")) {//입력 자료 검사
					JOptionPane.showMessageDialog(this, "수량 입력");
					txtSu.requestFocus();
					return;
				}
				if(txtDan.getText().equals("")) {//입력 자료 검사
					JOptionPane.showMessageDialog(this, "단가 입력");
					txtDan.requestFocus();
					return;
				}
				
				//수량과 단가는 숫자
				int su = 0;
				try {
					su = Integer.parseInt(txtSu.getText().trim());
					
				}catch (Exception e1) {
					JOptionPane.showMessageDialog(this, "수량은 숫자만 허용!");
					txtSu.requestFocus();
					return;
				}
				int dan = 0;
				try {
					dan = Integer.parseInt(txtDan.getText().trim());
					
				}catch (Exception e1) {
					JOptionPane.showMessageDialog(this, "수량은 숫자만 허용!");
					txtDan.requestFocus();
					return;
				}
				
				//등록 가능한 상태
				try {
					conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
					
					//새상품 코드 구하기(가장 큰 값을 얻어서 auto increment)
					int new_code = 0;
					String sql = "select max(code) from sangdata";
					pstmt = conn.prepareStatement(sql);
					rs = pstmt.executeQuery();
					if(rs.next()) {
						new_code = rs.getInt(1) + 1; // 별명을 걸었으면 new_code = rs.getInt("max");
					}
					
					//상품 추가
					sql = "insert into sangdata values(?,?,?,?)";
					pstmt = conn.prepareStatement(sql);
					pstmt.setInt(1, new_code);
					pstmt.setString(2, txtSang.getText().trim());
					pstmt.setInt(3, su);
					pstmt.setInt(4, dan);
					if(pstmt.executeUpdate() > 0)    //int re = pstmt.executeUpdate(); if(re > 0) {}
						JOptionPane.showMessageDialog(this, "등록 성공");
					else 
						JOptionPane.showMessageDialog(this, "등록 실패");

				} catch (Exception e2) {
					System.out.println("신 상품 추가 에러\t" + e2.getMessage());
				}finally {
					try {
						if(rs != null) rs.close();
						if(pstmt != null) pstmt.close();
						if(conn != null) conn.close();						
					}catch (Exception e1) {
						System.out.println("DB Close err\t" + e1.getMessage());
					}
				}
				
			}else if(e.getSource() == btnCancel) { //입력 자료 초기화
				txtSang.setText("");
				txtSu.setText("");
				txtDan.setText("");
			}
		}
	}
	/****/
	
	public static void main(String[] args) {
		new DbTest10Crd();
	}
}
