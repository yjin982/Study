package pack5;

public class Jepum_Tv extends Jepum{
	
	//생성자
	public Jepum_Tv() {
		System.out.println("TV 생성자");
	}
	
	//메소드
	@Override //추상클래스를 상속받기 때문에 반드시 오버라이드를 해야함
	public void volumeControl() {
		System.out.println("TV 소리 조절");
	}
}
