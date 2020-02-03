package pack6;

public class FlyerBall extends FlyerAdapter{ //Adapter 를 상속받았기때문에 원하는 메소드만 상속 받을 수 있음
	@Override
	public void fly() {
		System.out.println("야구공이 날아감");
	}
	
	public static void main(String[] args) {
		new FlyerBall().fly();
	}
}
