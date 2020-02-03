package sample;

import java.awt.Color;
import java.awt.Frame;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;


public class MyFrame6 extends Frame{
	
	public MyFrame6() {
		setTitle("내부 익명 클래스");
		setSize(400,300);
		setLocation(200, 200);
		setVisible(true);
		
		addWindowListener(new WindowAdapter() {
			@Override
			public void windowClosing(WindowEvent e) {
				System.exit(0);
			}
		});
		addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				int r = (int) (Math.random()*255);
				int g = (int) (Math.random()*255);
				int b = (int) (Math.random()*255);
				setBackground(new Color(r,g,b));
			}
		});
	}
	
	public static void main(String[] args) {
		new MyFrame6();
	}
}
