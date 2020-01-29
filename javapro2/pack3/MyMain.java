package pack3;

public class MyMain {

	public static void main(String[] args) {
		//응용 프로그램 시작점
		int kbs = 0;
		System.out.println("kbs : " + kbs);
		
		Car mycar1 = new Car();
		System.out.println(mycar1.wheel);
		mycar1.abc();
		//System.out.println(mycar1);//mycar1 객체의 주소 pack3.Car@7d6f77cc, 절대주소x
		//mycar1.airBag; //private 멤버이므로 접근 불가
		mycar1.showAirBag();
		int air = mycar1.getAirBag();
		System.out.println("air : " + air + ", getter :  " + mycar1.getAirBag());
		mycar1.setAirBag(123, 4);
		System.out.println("air : " + air + ", getter :  " + mycar1.getAirBag());
		
		
		
	}

}
