package pack5;

public final class Me extends Father{//final 클래스는 상속 불가능
	//멤버 변수
	public final int ABC = 10; //수정 불가
	
	//생성자
	public Me() {
		System.out.println("내 생성자");
	}
	
	//메소드
	public final void Biking() {//final메소드는 하위클래스에서 오버라이딩 불가능
		System.out.println("자전거로 전국일주");
	}
	@Override
	public String toString() {
		String ss = "자바 만세";
		return ss;
	}
	public void showMeData() {
		
	}
	
	//get,set
	@Override
	public int getNai() {
		return super.getNai();
	}
}
