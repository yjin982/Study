package pack1;

public class Test4 {

	public static void main(String[] args) {
		// 논리 연산자 처리 시 주의사항
		boolean a = false, b = true, c;
		c = a || b;
		System.out.println(c);
		c = a && b; // b까지 확인 안함
		System.out.println(c);
		System.out.println("-----------");
		
		boolean b1 = aa(),  b2;
		System.out.println(b1);
		System.out.println(bb());
		
		System.out.println("---or---");
		b2 = aa() || bb();
		System.out.println(b2); //bb()가 call 안 된 것을 확인가능
		b2 = bb() || aa();
		System.out.println(b2); //aa()까지 실행
		System.out.println("---and---");
		b2 = aa() && bb();
		System.out.println(b2);
		b2 = bb() && aa();
		System.out.println(b2);
		
		System.out.println();
		b2 = aa() | bb();//끝까지 검사 실행
		System.out.println(b2);
		b2 = bb() & aa();//끝까지 검사 실행
		System.out.println(b2);
		
		System.out.println("\n\n********");
	}
	
	public static boolean aa() {
		System.out.println("aa 수행");
		return true;
	}
	public static boolean bb() {
		System.out.println("bb 수행");
		return false;
	}

}
