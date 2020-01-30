package pack5;

public class HouseDog extends Dog{
	//멤버 변수
	private String where = "집";
	
	//생성자
	public HouseDog(String name) {
		super(name);
	}
	
	//메소드
	public void show() {
		System.out.println("거주 : " +where+ " 안");
	}
	@Override
	public void print() {
		System.out.println(getName() + " 는(은) "+ where + "에 살고 있다");
	}

}
