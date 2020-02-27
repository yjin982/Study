package pack2;

public class MyInterMain {
	public static void main(String[] args) {
		//1) 전통적 방법 : 인자가 없는 void 추상 메소드
		MyInterface inter = new MyInterface() {
			@Override
			public void abc() {
				System.out.println("일반적인 익명 클래스의 메소드 오버라이딩");
			}
		};
		inter.abc();
		
		//1) 람다식
		MyInterface inter2 = () -> { 
			System.out.println("일반적인 익명 클래스의 람다식 메소드 오버라이딩"); 
			System.out.println("일반적인 익명 클래스의 람다식 메소드 오버라이딩22"); 
		};
		inter2.abc();
		
		MyInterface inter3 = () -> System.out.println("일반적인 익명 클래스의 람다식 메소드 오버라이딩333"); 
		inter3.abc();
		
		System.out.println("──────────────────────────────────────");
		
		//2) 전통적 방법 : 인자가 있는 void 추상 메소드
		MyInterArg interArg = new MyInterArg() {
			@Override
			public void def(int a, int b) {
				System.out.println("두 수의 합은 " + (a+b));
			}
		};
		interArg.def(4, 3);
		
		//2) 람다식
		MyInterArg interArg2 = (a,b) -> System.out.println("두 수의 합은 " + (a+b) + " 22");
		interArg2.def(4, 3);
		MyInterArg interArg3 = (a,b) -> System.out.println("두 수의 곱은 " + (a*b) + " 333");
		interArg3.def(4, 2);
		MyInterArg interArg4 = (a,b) -> {
			int c = a*b;
			System.out.println("두 수의 곱은 " + c + " 4444");
		};
		interArg4.def(4, 2);
		
		System.out.println("──────────────────────────────────────");
		
		//3) 전통적 방법 : 반환값이 있는 추상 메소드
		MyInterArgOther other = new MyInterArgOther() {
			@Override
			public int def(int a, int b) {
				return a+b;
			}
		};
		int result = other.def(3, 4);
		System.out.println("result : " + result);
		
		
		//3) 람다식
		MyInterArgOther other2 = (m, n) -> { return m+n; };
		int result2 = other2.def(3, 4);
		System.out.println("result2 : " + result2);
		
		MyInterArgOther other3 = (m, n) -> m + n;
		int result3 = other3.def(3, 4);
		System.out.println("result3 : " + result3);
			
	}
}
