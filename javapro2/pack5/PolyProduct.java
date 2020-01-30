package pack5;

public class PolyProduct { //가전제품의 부모(원형, 슈퍼) 클래스
	//멤버 변수
	private int volume = 0;
	
	//메소드
	public void volumeControl() {
		//오버라이드를 기대
	}
	
	//get,set
	public int getVolume() {
		return volume;
	}
	public void setVolume(int volume) {
		this.volume = volume;
	}
}
