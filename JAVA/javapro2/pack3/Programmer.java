package pack3;

public class Programmer {
	public String nickName; //초기값 null
	private int age;  		  //초기값 0
	String spec = "자바, C, python";
	
	public static String moto = "미치자"; //static은 프로그램이 끝날 때까지 사용가능
//	public final double PI = 3.14;		//final은 수정이 불가, final 변수는 대문자로 쓰기
	public final static double PI = 3.14;
	
	
	public Programmer() {
		System.out.println("생성자, 생략 가능");
		age = 20;
	}
	public void displayData() {
		String re = reSpec();
		System.out.println("별명이 " + nickName + "은 " + age + "살 " + re);
	}
	private String reSpec() {
		return "보유 기술은 " + spec;
	}
	public void setAge(int age) {
		this.age = age;
	}
	public int getAge() {
		return age;
	}
	
	public static void staticMethod() {
//		System.out.println("age : " + age); //static메소드는 일반 멤버 호출x
		System.out.println("moto : " + moto);
	}
}

