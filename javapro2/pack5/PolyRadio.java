package pack5;

public class PolyRadio extends PolyProduct{
	//메소드
	@Override
	public void volumeControl() {
		System.out.println("라디오 소리 조절 후 : " + getVolume());
	}
}
