package pack1;

import java.awt.BorderLayout;
import java.awt.Button;
import java.awt.CardLayout;
import java.awt.Color;
import java.awt.Frame;
import java.awt.GridLayout;
import java.awt.Label;
import java.awt.Panel;
import java.awt.TextField;
import java.awt.event.*;

/***** BorderLayout(east, west, south, north, center), FlowLayout(좌->우, 상->하), GirdLayout(행렬), CardLayout(레이아웃 겹치기)  ...  *****/
public class LayoutTeat extends Frame implements ActionListener {
	/**멤버 변수**/
	// 패널 생성 / Panel은 FlowLayout이 기본
	Panel pn1 = new Panel(); // Visual Object(Component)을 담을 수 있는 Container 클래스
	Panel pn2 = new Panel(); // Frame 안에 포함
	Panel pn3 = new Panel();
	Panel pn4 = new Panel();
	Panel pn5 = new Panel();
	CardLayout card = new CardLayout(); // 카드 레이아웃
	Button btnOk;
	TextField txtBun, txtIrum;
	
	
	
	/**생성자**/ // Frame은 BorderLayout이 "기본"이나 여기에서는 GridLayout으로 변경
	public LayoutTeat() {
		setLayout(new GridLayout(2, 1)); // 2행 1열 그리드
		//// 1행
		Label lbl1 = new Label("bunho : ");
		txtBun = new TextField("10", 20);
		pn1.add(lbl1);
		pn1.add(txtBun);
		pn1.setBackground(Color.YELLOW);
//		add(pn1);   // Frame에 pn1을 포함
		Label lbl2 = new Label("Irum : ");
		txtIrum = new TextField("홍길동", 20);
		pn2.add(lbl2);
		pn2.add(txtIrum);
		pn2.setBackground(Color.CYAN);
//		add(pn2);
		
		//// Panel을 FlowLayout에서 CardLayout으로 변경
		pn3.setLayout(card);
		pn3.add("aa", pn1); //pn1을 카드 이름 aa로 지정
		pn3.add("bb", pn2);
		btnOk = new Button("ok");
		btnOk.setSize(60, 20);
		btnOk.addActionListener(this); // -> actionPerformed
		pn4.add(pn3);  // pn4는 FlowLayout
		pn4.add(btnOk);
		add(pn4); // Frame에 pn4 포함 (카드로 겹쳐진 pn1,pn2)
		
		//// 2행
		pn5.setBackground(Color.RED);
		pn5.setLayout(new BorderLayout());
		pn5.add("Center", new Label("Center", Label.CENTER));
		pn5.add("East", new Label("East"));
		pn5.add("West", new Label("West"));
		pn5.add("South", new Label("South", Label.CENTER));
		pn5.add("North", new Label("North", Label.CENTER));
		add(pn5);
		
		
		setTitle("레이아웃 연습");
		setBounds(200, 200, 400, 300);
		setVisible(true);
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
	}
	
	/**메소드**/
	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getActionCommand().equalsIgnoreCase("ok")) { // 버튼이 눌리면
			btnOk.setLabel("Clicked");
			card.show(pn3, "bb"); // 카드 레이아웃이 보여지게
			
		}else {
			btnOk.setLabel("Ok");
			card.show(pn3, "aa"); // pn3 안의 bb=pn2
		}
	}
	
	/**=== MAIN ===**/
	public static void main(String[] args) {
		new LayoutTeat();
	}
}
