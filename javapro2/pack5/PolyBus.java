package pack5;

public class PolyBus extends PolyCar{
	//멤버 변수
	private int passenger = 10;
	
	//생성자
	
	
	//메소드
	public void show() {
		System.out.println("버스");
	}
	@Override
	public void dispData() {
		System.out.println("버스의 승객 수는 "+passenger);
		System.out.println("버스의 속도는 "+ speed);
	}
	
	//get,set
	

}
