package pack1;

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class DbTest5RecMove extends JFrame implements ActionListener{
	/**멤버 변수**/
	JButton btnFirst, btnPre, btnNext, btnLast;
	JTextField txtNo, txtName;
	
	Connection conn;
	Statement stmt;
	ResultSet rs;
	
	
	/**생성자**/
	public DbTest5RecMove() {
		layInit();
		accDb();
		
		setTitle("레코드 이동");
		setBounds(750, 100, 400, 600);
		setVisible(true);
//		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		addWindowListener(new WindowAdapter() { //프로그램 종료하면서 db 연결 종료하도록
			@Override
			public void windowClosing(WindowEvent e) {
				try {
					if(rs != null) rs.close();
					if(stmt != null) stmt.close();
					if(conn != null) conn.close();
				} catch (Exception e2) {
					System.out.println("DB Access Close err\t" + e2.getMessage());
				}
				System.exit(0); //프로그래머 의도에 의해 정상 종료 0, 뜻하지않은 의도로 비정상 종료 1
			}
		});
	}
	
	
	/**메소드**/
	private void layInit() {
		txtNo = new JTextField("", 5);
		txtName = new JTextField("", 10);
		txtNo.setEditable(false);
		txtName.setEditable(false); //단순히 정보를 뿌리기 위한 용도, 원래는 label을 쓰는게 좋음, 단순히 박스로 둘러싼 형태로 보기위해
		
		JPanel panel1 = new JPanel();
		panel1.add(new JLabel("직원 자료 : "));
		panel1.add(txtNo);
		panel1.add(txtName);
		add("North", panel1);
		
		btnFirst = new JButton("|<<");
		btnPre = new JButton("<");
		btnNext = new JButton(">");
		btnLast = new JButton(">>|");
		JPanel panel2 = new JPanel();
		panel2.add(btnFirst);
		panel2.add(btnPre);
		panel2.add(btnNext);
		panel2.add(btnLast);
		add("Center", panel2);
		
		btnFirst.addActionListener(this);
		btnPre.addActionListener(this);
		btnNext.addActionListener(this);
		btnLast.addActionListener(this);		
	}
	private void accDb() {
		try {
			Class.forName("org.mariadb.jdbc.Driver");
			conn = DriverManager.getConnection("jdbc:mysql://127.0.0.1:3306/test", "root", "123");
			
			/* 원래는 ResultSet.TYPE_FORWARD_ONLY가 기본(순방향)
			ResultSet.TYPE_SCROLL_INSENSITIVE 순/역방향 가능, 편집 불가능
			ResultSet.TYPE_SCROLL_SENSITIVE 순/역방향 가능, 편집 가능 */
			stmt = conn.createStatement(ResultSet.TYPE_SCROLL_INSENSITIVE, ResultSet.CONCUR_READ_ONLY);
			
			rs = stmt.executeQuery("select jikwon_no, jikwon_name from jikwon"); //오라클은 sort가 안되서 order by 넣어주는게 좋음
			
			rs.next(); //첫 레코드로 이동시킴
			displayData();
			
		} catch (Exception e) {
			System.out.println("DB Access err\t" + e.getMessage());
		}
	}
	private void displayData() { //데이터출력
		try {
			txtNo.setText(rs.getString("jikwon_no"));
			txtName.setText(rs.getString("jikwon_name"));
			
		} catch (Exception e) {
			System.out.println("Display data err\t" + e.getMessage());
			JOptionPane.showMessageDialog(this, "자료의 처음 또는 마지막입니다.");
		}
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			//ResultSet.TYPE_SCROLL_INSENSITIVE를 썼기 때문에 first, last 등의 메소드가 가능ㅁ
			if(e.getSource() == btnFirst) rs.first();
			else if(e.getSource() == btnPre) rs.previous();
			else if(e.getSource() == btnNext) rs.next();
			else if(e.getSource() == btnLast) rs.last();
			
			displayData();
		}catch (Exception e1) {
			System.out.println("ActionPerformed err\t" + e1.getMessage());
		}
	}
	
	
	/**메인**/
	public static void main(String[] args) {
		new DbTest5RecMove();
	}
}
