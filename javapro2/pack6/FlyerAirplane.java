package pack6;

public class FlyerAirplane implements Flyer{
	
	@Override
	public void fly() {
		System.out.println("엔진 소리를 힘차게 내며 구름 속으로 날아감");
	}
	public boolean isAnimal() {
		return false;
	}
	
}
