package pack5;

public class WolfDog extends Dog{
	//멤버 변수
	private String where = "산";
	
	//생성자
	public WolfDog(String name) {
		super(name);
	}
	public WolfDog(String name, String where) {
		super(name);
		this.where = where;
	}
	
	//메소드
	public void show() {
		System.out.println("거주(wolf) : " +where+ " 속");
	}
	@Override
	public void print() {
		System.out.println(getName() + " 는(은) "+ where + "에 살고 있다?");
	}
	public void display() {
		print();
		this.print();
		super.print();
	}
	
	//
}
