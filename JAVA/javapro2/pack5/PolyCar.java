package pack5;

public class PolyCar {
	//멤버 변수
	protected int speed = 50;
	
	//생성자
	public PolyCar() {
		System.out.println("나는 자동차");
	}
	
	//메소드
	public void dispData() {
		System.out.println("속도는 "+speed);
	}
	
	//get,set
	public int getSpeed() {
		return speed;
	}
	
}
