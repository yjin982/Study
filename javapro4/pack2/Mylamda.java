package pack2;

public class Mylamda {
	
	static class Inner implements HelloInter{
		@Override
		public int addData(int a, int b) {
			return a+b;
		}
	}
	
	public static void main(String[] args) {
		Inner inner = new Inner();                    //전통적 방법
		System.out.println(inner.addData(3, 4));
		
		//인터페이스 변수 ==> 람다식 (익명 메소드)
		HelloInter hinter = (x, y) -> x + y;
		System.out.println(hinter.addData(3, 4));
		
		HelloInter hinter2 = (x, y) -> x * y;
		System.out.println(hinter2.addData(3, 4));
		
		
		
	}

}
