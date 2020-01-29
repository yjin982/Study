package pack1;

public class Test3 {

	public static void main(String[] args) {
		//관계, 논리 연산자, 기타
		int a = 5;
		System.out.println(a > 3);
		System.out.println(a <= 3);
		System.out.println(a == 3);
		System.out.println(a != 3);
		System.out.println();
		
		int b = 10;
		System.out.println(a > 3 && b <= 10); //and
		System.out.println(a > 3 && b != 10);
		System.out.println(a > 6 || b <= 10); //or
		System.out.println(a > 6 || b != 10);
		System.out.println();
		
		int ii = 8, ij;
//		System.out.println(ii + " " + ij); //The local variable ij may not have been initialized
		System.out.println("ii: " + ii + ", ii binary: " + Integer.toBinaryString(ii));
		ij = ii << 1; //shift 연산자
		System.out.println("ij: " + ij + ", ij binary: " + Integer.toBinaryString(ij));
		ij = -ii >> 2; //우로 2bit, 남는 좌측은 부호와 같은 값으로 채움
		System.out.println("ij : " + ij + ", ij binary: " + Integer.toBinaryString(ij));
		ij = ii >>> 2;//우로 2bit, 남는 좌측은 0으로 채움
		System.out.println("ij : " + ij + ", ij binary: " + Integer.toBinaryString(ij));
		System.out.println();
		
		//삼항 연산자
		int re = (ii < 5)? 100 : 50+20; // 변수 = 조건? 참:거짓
		System.out.println("re : " + re);
		
		int x,y,z;
		x = y = z = 5;
		System.out.println(x + " " + y + " " + z);
		
		aa(); //method call
		bb(11);
		
		System.out.println("프로그램 종료");
	}
	
	public static void aa () { //성격이 비슷한 명령문들을 모아놓은 집단 = 메소드
		System.out.println("aa 메소드 수행");
		bb(12);
	}
	
	public static void bb (int mbc) {
		System.out.println("bb 메소드 처리, mbc: " + mbc);
	}

}
