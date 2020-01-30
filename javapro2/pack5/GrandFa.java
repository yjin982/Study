package pack5;

public class GrandFa {
	//멤버 변수
	private int nai = 80;
	public String gabo = "상감청자";
	protected String gahun = "객체를 이해하자";
	
	//생성자
	public GrandFa() {
		System.out.println("할아버지 생성자");
	}
	public GrandFa(int nai) {
		this(); //현재 클래스 내의 생성자가 다른 생성자(argument가 일치하는)를 호출을 먼저하고 다른 statement를 실행.
		this.nai = nai;
		//this(); 이 위치는 불가능
	}
	
	//메소드
	public String say() {
		return "할아버지 말씀 : 데이터 사이언티스트가 되거라";
	}
	public void eat() {
		System.out.println("밥은 맛있게");
	}
	
	//getter
	public int getNai() {
		return nai;
	}
}
