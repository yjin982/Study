package pack1;

public class Test2 {

	public static void main(String[] args) {
		//연산자 우선순위 () > 산술연산(*,/  >  +,-) > 관계 > 논리 > =(치환)
		
		int a = 5; //치환
		int b = 3;
		int c = a + b;
		
		//산술 연산자
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println(a*b);
		System.out.println(a/b); //몫
		System.out.println(a%b); //나머지
		System.out.println((double)a/b);
		
//		System.out.println(a/0); // 에러(/ by zero)로 이 뒤에는 실행안됨
		System.out.println(a/0.0); //Infinity
		System.out.println(a%0.0); //NaN
		System.out.println(0 / 0.0); //NaN
		
		System.out.println(3+4*5);
		System.out.println((3+4)*5);
		
		String ss1 = "대한";
		String ss2 = "민국";
		String ss3 = ss1 + ss2;
		System.out.println("ss3 = " + ss3);
		System.out.println("ss3 = " + ss3 + "2020");
		System.out.println("ss3 = " + ss3 + 2020);
		System.out.println("ss3 = " + ss3 + Integer.toString(2020));
		System.out.println(10 + 20);
		System.out.println(10 + "20");
		System.out.println(10 + Integer.parseInt("20") + "\n\n");
		
		//누적
		int no = 1;
		no = no + 1;
		no += 1;
		no++; ++no;
		System.out.println("no : " + no);
		
		//증감 연산자
		int imsi = 5;
		int result = ++imsi +1;
		System.out.println(imsi + " / " + result);
		
		int imsi2 = 5;
		int result2 = imsi2++ +1;//+먼저 ++은 나중
		System.out.println(imsi2 + " / " + result2);
		
		//부호
		int imsi3 = 3;
		System.out.println("imsi3:"+ imsi3 + ", -imsi3:" + -imsi3 + ", -imsi3*-1:" + -imsi3 * -1);
		
//		System.exit(0); //강제종료
		System.out.println("프로그램 종료");
	}

}
