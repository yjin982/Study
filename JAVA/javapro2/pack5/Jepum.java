package pack5;

public abstract class Jepum { //추상 메소드를 하나라도 가지고 있으면 추상 클래스
	//멤버 변수
	public int volume = 0;
	
	//생성자
	public Jepum() {
		System.out.println("Jepum 추상 클래스 생성자");
	}
	
	//메소드
	abstract public void volumeControl(); //추상 메소드  
	public void volumeShow() {
		System.out.println("소리 크기 : " + volume);
	}
}
