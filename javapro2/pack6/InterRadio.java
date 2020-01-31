package pack6;

public class InterRadio implements InterVol, InterVol2{ //다중 상속 효과
//public class InterRadio implements InterVol{ // 이 경우 up,down 은 오버라이드, off,resume은 일반메소드처리
//public class InterRadio implements InterVol2{// 이 경우 up,down 은 일반메소드, off,resume은 오버라이드 처리
//public class InterRadio { //셋 다 가능 (오버라이드 된 함수냐 아니냐의 차이)
	private int v = 0;
		
	public void volUp(int v) {
		this.v += v;
	}
	public void volDown(int v) {
		this.v -= v;
	}
	public void volOff() {
		System.out.println("라디오 끄기");
	}
	public void volResume() {
		System.out.println("라디오 켜기");
	}
	
	public void show() {
		System.out.println("현재 볼륨은" + v);
	}
}
