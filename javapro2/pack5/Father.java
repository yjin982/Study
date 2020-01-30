package pack5;

public class Father extends GrandFa{ //부모,super,parent,조상 | 자식,sub,child,파생
	//멤버 변수
	private int nai = 55;
	private int house = 1; //현재 클래스의 고유 멤버
	public String gabo = "꽃병";  //은닉화 : 부모의 멤버가 숨겨짐
	protected String gahun = "다형성을 이해하자";
	
	//생성자
	public Father() {
		super(); 		//부모 생성자 호출, argument에 의해 선택적으로 호출
		System.out.println("아버지 생성자");
	}
	
	//메소드
	@Override // annotation : 부모 메소드와 동일해야함을 강요
	public String say() { //부모 메소드와 동일한 메소드를 선언 : 메소드 오버라이드
		return "자바 프로그래머 전문가가 되자";
	}
	@Override
	public void eat() {
		System.out.println("빵도 맛있다");
	}
	public void showData() {
		String gabo = "컴퓨터";
		System.out.println("가보 : " + gabo); // == 지역변수가 없을 때, this.gabo
		System.out.println("가보 : " + this.gabo);
		System.out.println("가보 : " + super.gabo);
		System.out.println("나이 : " + this.getNai());
		System.out.println("나이 : " + super.getNai());
		this.eat();
		super.eat();
	}
	
	//get,set
	@Override
	public int getNai() { 
		return this.nai;
	}

}
