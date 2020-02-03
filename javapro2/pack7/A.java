package pack7;

public class A { // 가장 바깥쪽 클래스
	/*****멤버*****/
	int field1;
		
	/*****생성자*****/
	public A() {
		System.out.println("	A 생성자");
	}
	
	/*****메소드*****/
	void method1( ) {
		System.out.println("	method1 수행 : " + field1);
	}
	
	void a_method4() { //A클래스의 메소드
		System.out.println("	a_method4가 진행"); 
		
		class D{//local class*****/
			int field5;
			public D() {
				System.out.println("		D 생성자");
			}
			void method5() {
				System.out.println("		method5 수행 : " + field5);
			}
		}
		
		D d = new D();
		d.field5 = 5;
		d.method5();
	}
	
	
	/*****내부 클래스*****/
	class B{ ////////////////가장 흔한 패턴
		//멤버
		int field2;
		//생성자
		public B() {
			System.out.println("	B 생성자");
		}
		//메소드
		void method2( ) {
			System.out.println("	method2 수행 : " + field2);
		}		
	}
	
	//정적 멤버 클래스 *****/
	static class C {
		//멤버
		int field3;
		//생성자
		public C() {
			System.out.println("	C 정적 객체 생성자");
		}
		//메소드
		void method3( ) {
			System.out.println("	method3 수행 : " + field3);
		}	
	}
	/***************/
	
	
	/*=====허용 범위=====*/
	B b2 = new B();
	C c2 = new C();
//	D d2 = new D(); //메소드 안에 존재하기 때문에 불가능
	
	void test1() {
		B b3 = new B();
		C c3 = new C();
	}
	
	static C c4 = new C();
	static void test2() {
//		B b4 = new B(); //static 메소드는 static만 처리 가능, B는 static이 아님
		C c5 = new C(); 
	}
	
	/*==========*/
	
	
	
	/*****메인*****/
	public static void main(String[] args) {
		A a = new A();
		a.field1 = 1;
		a.method1();
		
		System.out.println("인스턴스 멤버 클래스");
		A.B b = a.new B();
		b.field2 = 2;
		b.method2();
		
		System.out.println("정적 인스턴스 멤버 클래스");
		A.C c = new A.C();
		c.field3 = 3;
		c.method3();
		C c2 = new C(); //static
		c2.field3 = 4;
		c2.method3();
		
		System.out.println("로컬 클래스 멤버");
		a.a_method4();
		
		System.out.println("\n===============");
		a.test1();
		test2(); // a.test2(); 가능하지만 권장사항이 아님(static)
	}
	
}
