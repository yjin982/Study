package pack6;

//내부 클래스 연습 : 클래스의 내의 클래스를 선언
public class Outer {
	//멤버 변수
	private int a;
	Inner innter;
	
	//생성자
	public Outer() {
		System.out.println("Outer 생성자");
		a = 10;
		innter = new Inner();
	}
	
	//메소드
	public void aa() {
		System.out.println("Outer : aa 메소드");
		System.out.println("Outer의 a는 " + a);
		bb();
		innter.cc();
		System.out.println("Outter의 a는 " + a + ", Inner의 b는 " + innter.b);
		
	}
	public void bb() {
		System.out.println("Outer : bb 메소드");
	}
	
	/*****내부 클래스*****/
	class Inner{
		int b;
		
		public Inner() {
			System.out.println("Inner 생성자");
			b = 20;
		}
		
		public void cc() {
			System.out.println("Inner : cc 메소드");
			System.out.println("Inner의 b는 " + b + ", Outter의 a는 " + a);
			bb(); //내부 클래스는 외부클래스의 멤버도 제한없이 사용가능
		}
		
		/*****내부의 내부 클래스*****/
		public class InnerInner {		/*가능하지만 권장 사항이 아님*/		}
	}
	
	/*****MAIN*****/
	public static void main(String[] args) {
		Outer outer = new Outer();
		outer.aa();
		
		 System.out.println();
		 
//		 Inner inner = new Inner(); // X : Inner클래스는 Outer 클래스 안에서만 사용가능하므로 
//		 Outer.Inner innter = outer.new Inner();
//		 innter.cc();  O : 가능하지만 이런식으로 잘 하지 않음
//		 innter 클래스는 outer 클래스 전용이기 때문에 외부에서 잘 호출하지 않음
	}
}
