package pack5;

public class PolyTaxi extends PolyCar{
	//멤버 변수
	private int passenger = 2;
	
	//생성자
	
	
	//메소드
	public void show() {
		System.out.println("택시");
	}
	@Override
	public void dispData() {
		System.out.println("택시의 승객 수는 "+passenger);
	}
	
	//get,set
	

}
