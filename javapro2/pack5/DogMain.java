package pack5;

public class DogMain {

	public static void main(String[] args) {
		Dog dog = new Dog();
		dog.print();
		System.out.println(dog.callName());
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
		
		HouseDog hd = new HouseDog("집개");
		hd.print();
		hd.show();
		System.out.println(hd.callName());
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
		
		WolfDog wd = new WolfDog("늑대");
		wd.print();
		wd.show();
		System.out.println(wd.callName());
		wd.display();
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
		
		WolfDog bushdog = wd; //같은 객체를 참조
		bushdog.print(); // == wd.print();
		
		//Promotion
		Dog dog2 = wd; //Dog가 상위 클래스이므로 WolfDog 객체 참조 가능
		dog2.print();     // wd와 같은 print(); 부모객체 타입이면서 자식객체의 메소드 호출(단, 오버라이딩 된 메소드만 가능)
//		dog2.dispaly(); // 에러 = WolfDog의 고유 메소드는 호출 불가능 => 불간섭의 원칙
		
		//Casting
		bushdog = (WolfDog)dog2; //기본적으로 부모타입은 자식타입에게 넘겨주기 불가능
		bushdog.print();
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
		//다형성
		Dog coyote = new Dog("코요테");
		coyote.print();
		coyote = bushdog;
		coyote.print();
		coyote = hd;
		coyote.print();
	}

}
