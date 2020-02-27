package pack1;
/*
 * 단축키 줄 맞춤 ctrl+shift+f
 */
public class Test1 {
	public static void main(String args[]) {
		System.out.println("a");
		System.out.print("b");
		System.out.println("c");
		
		//변수 : 기본형
		byte var1 = 10; // 1byte 정수 2^7 = -128~127 (8bit중 맨 처음은 sign bit이므로)
		System.out.println("var1 : " + var1);
		System.out.println(Byte.MAX_VALUE + " ~ " + Byte.MIN_VALUE);
		
		short var2 = 32767; //2byte 2^15 -32768~32767
		System.out.println("var2 : " + var2);
		
		int var3 = 214748364; //4byte 2^31
		System.out.println("var3 : " + var3);
		
		long var4 = 3114748364L; //8byte 2^63, long형은 쓸 때 뒤에 L을 추가
		System.out.println("var4 : " + var4);
		
		//promotion : 자동 형변환, cast : 강제 형변환
		byte b1 = 12; //12 int가 자동으로 byte로 들어감 = promotion
		byte b2 = (byte) 128; //cast 강제로 최대값 이상 넣어서 쓰레기값 들어감
		System.out.println("b2 : " + b2);
		
		int b3 = 10;
		byte b4 = (byte) b3; //cast
		System.out.println("b4 : " + b4);
		short s1 =10;
		int i1 = s1; //promotion
		System.out.println("i1 : " + i1);
				
		System.out.println("\n\n-----실수처리-----");
		double d1 = 10.5; // print 10.5
		d1 = 5; //promotion
		System.out.println("d1 : " + d1);
		float f1 = (float) 4.5; //실수 기본형은 double = cast해주기
		f1 = 5.1F; //float 명시
		System.out.println("f1 : " + f1);
		
		int i2 = (int) 3.5;
		System.out.println("i2 : " + i2); //소수점 아래 버림
		double d2 = 4.5+10;
		System.out.println("d2 : " + d2);//연산시 큰 타입으로 자동 형변환
		
		boolean bu = true; //boolean은 true or false
		System.out.println("\nboolean : " + bu);
		
		char c1 = 'a'; //char은 ' '  , " " 은 string
		System.out.println("c1 : " + c1 + " / " + (int)c1 + " " + (char)97); //소문자 a 아스키코드값이 97 / 대문자 65 / 숫자0 48
		
		//아스키코드 10 = LF(line feed), 13 = CR(carriage return)  ==  엔터
		System.out.println("안녕" + "\n" + "반가워");
		System.out.println("안녕" + (char)10 + "반가워");
		System.out.println("안녕" + (char)13 + "반가워");
		
		System.out.println(0xa +" "+ 0xf); //hex 16진수
		System.out.println(05 +" "+ 052 + "\n\n"); //octal 8진수
		
	
		//변수 : 참조형
		String irum = "홍길동"; //대문자로 시작 = class라는 뜻 = char를 배열로 만들어서 변수처럼 사용하게 만듦 
		System.out.println(irum); //irum은 홍길동이란 배열이 저장된 곳의 주소를 저장
	}
}
