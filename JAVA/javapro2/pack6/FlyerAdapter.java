package pack6;

//Adapter Class
public abstract class FlyerAdapter implements Flyer{
	//인터페이스를 상속 받아 추상 클래스 안의 일반 메소드들로 만들어서 자식이 원하는 메소드만 사용할 수 있도록 함
	
	@Override
	public void fly() {}
	@Override
	public boolean isAnimal() {
		return false;
	}
}
