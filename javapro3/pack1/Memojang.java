package pack1;

import java.awt.Color;
import java.awt.FileDialog;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JMenu;
import javax.swing.JMenuBar;
import javax.swing.JMenuItem;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JPopupMenu;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;

public class Memojang extends JFrame implements ActionListener{
	/**멤버 변수**/
	private JButton btnCopy = new JButton("copy");
	private JButton btnPaste = new JButton("paste");
	private JButton btnCut = new JButton("cut");
	private JButton btnDel = new JButton("del");
	private JPanel pn = new JPanel();
	private JTextArea txtMemo = new JTextArea("", 10, 30);
	private String copyText;
	////////////////////////////메뉴바////////////////////////////////////////
	JMenuItem mnuNew, mnuSave, mnuOpen, mnuExit;
	JMenuItem mnuCopy, mnuPaste, mnuCut, mnuDel;
	JMenuItem mnuAbout, mnuEtc1, mnuEtc2;
	///////////////////////////팝업메뉴/////////////////////////////////////////
	JPopupMenu popup;
	JMenuItem m_white, m_cyan, m_pink;
	
	
	/**생성자**/
	public Memojang() {
		super("*제목 없음 - 간단 메모장");
		initLayout();
		menuLayout();
		
		setBounds(300, 300, 500, 400);
		setVisible(true);
		
//		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // 종료 의사 묻기 불가능
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				int re = JOptionPane.showConfirmDialog(Memojang.this, "정말 종료할까요?", "종료", JOptionPane.YES_NO_OPTION);
				
				if(re == JOptionPane.YES_OPTION)
					setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				else
					setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);
			}
		});
	}
	
	
	/**메소드**/
	private void initLayout() { //디자인
		pn.add(btnCopy);
		pn.add(btnPaste);
		pn.add(btnCut);
		pn.add(btnDel);
		add("South", pn);
		
		JScrollPane scrollpane = new JScrollPane(txtMemo); // 스크롤판에 txtArea 포함
		add("Center", scrollpane);
		
		btnCopy.addActionListener(this);
		btnPaste.addActionListener(this);
		btnCut.addActionListener(this);
		btnDel.addActionListener(this);
	}
	private void menuLayout() { //메뉴 디자인 추가
		JMenuBar menubar = new JMenuBar();
		
		JMenu mnuFile = new JMenu("파일"); // 주메뉴
		mnuNew = new JMenuItem("새로 만들기");
		mnuSave = new JMenuItem("저장..."); // ... : 부메뉴 혹은 추가 작업이 있다는 의미
		mnuOpen = new JMenuItem("열기...");
		mnuExit = new JMenuItem("종료");
		mnuFile.add(mnuNew);
		mnuFile.add(mnuOpen);
		mnuFile.add(mnuSave);
		mnuFile.addSeparator(); // 구분선
		mnuFile.add(mnuExit);
		
		JMenu mnuEdit = new JMenu("편집"); 
		mnuCut = new JMenuItem("잘라내기");
		mnuCopy = new JMenuItem("복사");
		mnuPaste = new JMenuItem("붙여넣기");
		mnuDel = new JMenuItem("지우기");
		mnuEdit.add(mnuCut);
		mnuEdit.add(mnuCopy);
		mnuEdit.add(mnuPaste);
		mnuEdit.add(mnuDel);
		
		JMenu mnuHelp = new JMenu("도움말");
		mnuAbout = new JMenuItem("메모장이란...");
		JMenu mnuEtc = new JMenu("기타");
		mnuEtc1 = new JMenuItem("계산기");
		mnuEtc2 = new JMenuItem("프리셀");
		mnuHelp.add(mnuAbout);
		mnuEtc.add(mnuEtc1);
		mnuEtc.add(mnuEtc2);
		mnuHelp.add(mnuEtc); //메뉴에 부메뉴 등록
		
		menubar.add(mnuFile);  //메뉴바에 메뉴 등록
		menubar.add(mnuEdit);
		menubar.add(mnuHelp);
		setJMenuBar(menubar); //프레임에 메뉴바 등록
		
		//메뉴는 액션리스너만 가능
		mnuNew.addActionListener(this);
		mnuSave.addActionListener(this);
		mnuOpen.addActionListener(this);
		mnuExit.addActionListener(this);
		mnuCut.addActionListener(this);
		mnuCopy.addActionListener(this);
		mnuPaste.addActionListener(this);
		mnuDel.addActionListener(this);
		mnuAbout.addActionListener(this);
		mnuEtc1.addActionListener(this);
		mnuEtc2.addActionListener(this);
		
		// 팝업 메뉴
		popup = new JPopupMenu();
		JMenu m_color = new JMenu("배경색 선택");
		m_white = new JMenuItem("하양");
		m_cyan = new JMenuItem("시안");
		m_pink = new JMenuItem("핑크");
		
		m_color.add(m_white);
		m_color.add(m_cyan);
		m_color.add(m_pink);
		
		popup.add(m_color);
		txtMemo.add(popup); // txtArea 에서 뜨기 때문에 여기에 추가
		
		m_white.addActionListener(this);
		m_cyan.addActionListener(this);
		m_pink.addActionListener(this);
		
		txtMemo.addMouseListener(new MouseAdapter() {
			@Override
			public void mousePressed(MouseEvent e) {
				if(e.getModifiers() == MouseEvent.BUTTON3_MASK) // 마우스 버튼은 3개로 구분
					popup.show(txtMemo, e.getX(), e.getY()); //이것만 쓰면 좌우 구분 X
			}
		});
	}
 	@Override
	public void actionPerformed(ActionEvent e) {
 		/** ----- 복사,잘라낸 텍스트가 다른 프로그램에서도 적용되게 하려면 클립보드를 이용 ----- **/
		if(e.getSource() == btnCopy || e.getSource() == mnuCopy) {
			copyText = txtMemo.getSelectedText(); // 선택된 부분만 카피
			
		}else if(e.getSource() == btnPaste || e.getSource() == mnuPaste) {
			int position = txtMemo.getCaretPosition(); //선택된 위치
			txtMemo.insert(copyText, position);

		}else if(e.getSource() == btnCut || e.getSource() == mnuCut) {
			copyText = txtMemo.getSelectedText();
			
			int start = txtMemo.getSelectionStart();
			int end = txtMemo.getSelectionEnd();
			
			txtMemo.replaceRange("", start, end);
			
		}else if(e.getSource() == btnDel || e.getSource() == mnuDel) {
			int start = txtMemo.getSelectionStart();
			int end = txtMemo.getSelectionEnd();
			
			txtMemo.replaceRange("", start, end);
			
		}else if(e.getSource() == mnuNew) {
			// ... 저장 사항이 없을 때 저장 여부 묻는 알림창 작업
			txtMemo.setText("");
			setTitle("*제목 없음 - 간단 메모장");
			
		}else if(e.getSource() == mnuOpen) {
			// ... 저장 사항이 없을 때 저장 여부 묻는 알림창 작업
			FileDialog dialog = new FileDialog(this, "저장", FileDialog.LOAD);
			dialog.setVisible(true); //창 보여주기
			
			if(dialog.getFile() == null) return;
			String dfName = dialog.getDirectory() + dialog.getFile();
			try {
				BufferedReader reader = new BufferedReader(new FileReader(dfName));

				txtMemo.setText("");
				String line;
				while((line = reader.readLine()) != null) {
					txtMemo.append(line + "\n");
				}
				reader.close();
				
				setTitle(dialog.getFile() + " - 간단 메모장");
			}catch (Exception err) {
				System.out.println("save err : " + err.getMessage());
			}
			
		}else if(e.getSource() == mnuSave) {
			//저장을 위한 경로명 및 파일명 등을 얻기 위한 운영체제의 대화상자 호출
			FileDialog dialog = new FileDialog(this, "저장", FileDialog.SAVE);
			dialog.setVisible(true); //창 보여주기
//			dialog.setDirectory("."); //
			
			if(dialog.getFile() == null) return;
			String dfName = dialog.getDirectory() + dialog.getFile();
			
			try {
				BufferedWriter writer = new BufferedWriter(new FileWriter(dfName));
				writer.write(txtMemo.getText());
				writer.close();
				
				setTitle(dialog.getFile() + " - 간단 메모장");
			}catch (Exception err) {
				System.out.println("save err : " + err.getMessage());
			}
			
		}else if(e.getSource() == mnuExit) {
			// ... 저장 사항이 없을 때 저장 여부 묻는 알림창 작업
			System.exit(0); 
			
		}else if(e.getSource() == mnuAbout) {
			new MemoAbout(this);
			System.out.println("대화 상자 호출 후");
			
		}else if(e.getSource() == mnuEtc1) {
			try {
				Runtime runtime = Runtime.getRuntime();
				runtime.exec("calc.exe");
			}catch (Exception err) {
				System.out.println(err.getMessage());
			}
		}else if(e.getSource() == mnuEtc2) {
			try {
				Runtime.getRuntime().exec("calc.exe");
			}catch (Exception err) {
				System.out.println(err.getMessage());
			}
		}else if(e.getSource().equals(m_white)) { // 비권장
			txtMemo.setBackground(Color.WHITE);
		}else if(e.getSource().equals(m_cyan)) {
			txtMemo.setBackground(Color.CYAN);
		}else if(e.getSource().equals(m_pink)) {
			txtMemo.setBackground(Color.PINK);
		}
		
		txtMemo.requestFocus(); // 포커스 안 써주면 버튼에 포커스가 있음
	}

	
	/**===MAIN===**/
	public static void main(String[] args) {
		new Memojang();
	}
}
