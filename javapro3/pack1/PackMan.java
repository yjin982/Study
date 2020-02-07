package pack1;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.Toolkit;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JFrame;

public class PackMan extends JFrame implements KeyListener{
	/**멤버 변수**/
	Image image;
	int  x, y, sel = 1;
	
	/**생성자**/	
	public PackMan() {
		super("상하좌우 화살표를 사용하세요");
		
		setIconImage(Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack1.jpg")); // 타이틀 아이콘 이미지
		setResizable(false); // 창 크기 고정
		setBackground(Color.WHITE);
		setLayout(null); // 레이아웃 사용 X
		setBounds(750, 200, 400, 400);
		setVisible(true);
		
		x = (int)getWidth() / 2; // 창 내의 좌표값
		y = (int)getHeight() / 2;
		
		addKeyListener(this);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	}
	
	
	/**메소드**/
	@Override
	public void paint(Graphics g) { //자동 호출
		switch (sel) {
		case 1: // 오른
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack1.jpg");
			break;
		case 2: // 오른 입 벌린
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack2.jpg"); 
			break;
		case 3: // 왼
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack3.jpg");
			break;
		case 4: // 왼 입 벌린
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack4.jpg");
			break;
		case 5: // 아래
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack5.jpg");
			break;
		case 6: // 아래 입 벌린
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack6.jpg");
			break;
		case 7: // 위
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack7.jpg");
			break;
		case 8: // 위 입 벌린
			image = Toolkit.getDefaultToolkit().getImage("c:/work/pack/pack8.jpg");
			break;
		}
		
		g.clearRect(0, 0, getWidth(), getHeight()); //화면을 클리어해서 잔상 해결
		g.drawImage(image, (x - image.getWidth(this) / 2), (y  - image.getWidth(this) / 2), this);
	}
	@Override
	public void keyPressed(KeyEvent e) {
//		System.out.println(e.getKeyCode());  //키 코드값 ←37   ↑ 38   →39  ↓40 , 키워드도 정리되어있음
		int key = e.getKeyCode(); // 키보드 눌려진 값을 받아옴.

		if(key == KeyEvent.VK_NUMPAD6 || key == KeyEvent.VK_RIGHT ||  key == KeyEvent.VK_D) { //오른쪽
			
			sel = (sel == 1)? 2:1;   /**----3항 연산자  변수=조건? 참:거짓; [if(sel==1) sel=2; else sel=1;] ----**/
//			System.out.println("x:" + x);//좌표값 확인용
			x = (x < getWidth())? x+10:-image.getWidth(this);
			/**----- x가 전진 시 10씩 커지는데(+값) 프레임 너비보다 커지면 이미지의 너비만큼 마이너스값을 x에 줘서 자연스럽게 들어오도록 함 -----**/
			
		}else if(key == KeyEvent.VK_NUMPAD4 || key == KeyEvent.VK_LEFT ||  key == KeyEvent.VK_A) { //왼
			
			sel = (sel == 3)? 4:3; //그림 방향 설정 -> paint -> switch
//			System.out.println("x:" + x);//좌표값 확인용
			x = (x > 0)? x-10:getWidth()+image.getWidth(this);
			/**----- x가 후진 시 10씩 작아지는데(+값) 프레임 너비보다 작아지면(-값) 프레임 너비+이미지의 너비만큼 플러스값을 x에 줘서 자연스럽게 들어오도록 함 -----**/
			
		}else if(key == KeyEvent.VK_NUMPAD8 || key == KeyEvent.VK_UP ||  key == KeyEvent.VK_W) { // 상
			
			sel = (sel == 7)? 8:7;
//			System.out.println("y:" + y);//좌표값 확인용
			y = (y > 0)? y-10:getHeight()+image.getHeight(this);
			
		}else if(key == KeyEvent.VK_NUMPAD2 || key == KeyEvent.VK_DOWN ||  key == KeyEvent.VK_S) { // 하
			
			sel = (sel == 5)? 6:5;
//			System.out.println("y:" + y);//좌표값 확인용
			y = (y < getHeight())? y+10:-image.getHeight(this);
			
		}
		
		repaint();
	}
	@Override
	public void keyReleased(KeyEvent e) {}
	public void keyTyped(KeyEvent e) {}
	
	
	/**===MAIN===**/
	public static void main(String[] args) {
		new PackMan();
	}
}
