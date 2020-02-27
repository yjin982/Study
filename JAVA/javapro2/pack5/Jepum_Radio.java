package pack5;

public class Jepum_Radio extends Jepum{
	
	//메소드
	@Override //추상클래스를 상속받기 때문에 반드시 오버라이드를 해야함
	public void volumeControl() {
		System.out.println("라디오 소리 업다운");
	}
}
