package pack5;

public class PolyMain {
	public static void main(String[] args) {
		PolyCar car1 = new PolyCar();
		car1.dispData();
		
		PolyBus bus1 = new PolyBus();
		bus1.dispData();
		bus1.show();
		
		PolyTaxi taxi1 = new PolyTaxi();
		taxi1.dispData();
		taxi1.show();
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
		PolyCar car2 = new PolyBus(); //promotion
		car2.dispData(); //polyBus의 메소드
		System.out.println(car2.getSpeed());
//		car2.show(); X //polyBus의 고유 메소드
		
		System.out.println();
		
		PolyCar car3 = new PolyTaxi();
		car3.dispData(); //polyTaxi의 메소드
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
//		PolyBus bus2 = new PolyCar(); // X
		PolyBus bus2 = (PolyBus)car2; //Casting 강제형변환
		bus2.dispData();
		bus2.show();
		
		System.out.println();
		//PolyTaxi taxi2 = new PolyCar() //X
		PolyTaxi taxi2 = (PolyTaxi)car3;  //O
//		PolyTaxi taxi3 = (PolyTaxi)car1;  // ClassCastException,  문법오류는 X
		
		System.out.println("======================");
		PolyCar p[] = new PolyCar[3];
		p[0] = car1;
		p[1] = bus1;
		p[2] = taxi1;
		for (int i = 0; i < p.length; i++) {
			p[i].dispData();
		}
		System.out.println();
		for(PolyCar car:p) {
			car.dispData();
		}
	}
}
