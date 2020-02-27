package pack3;

public class ProMain {

	public static void main(String[] args) {
		System.out.println("static, final ... ");
		
		Programmer tom = new Programmer();
//		tom.Programmer(); 		X
		System.out.println("tom : " + tom.spec);
		tom.displayData();
		tom.nickName = "자바도사";
		tom.displayData();
		tom.setAge(28);
		tom.displayData();
		System.out.println("나이는 " + tom.getAge());
		System.out.println(tom.moto);
		System.out.println(Programmer.moto);
		System.out.println(tom.PI); 
		System.out.println(Programmer.PI);
		Programmer.staticMethod(); //static은 객체명이 아니라 클래스명으로 호출
		
		System.out.println("---------------------");
		Programmer oscar = new Programmer();
		oscar.displayData();
//		oscar = null;
//		oscar.displayData(); 	//런타임에러 : 실행해봐야 알 수 있음
		oscar.setAge(33);
		oscar.displayData();
		
		
		
		
	}

}
