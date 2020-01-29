package pack3;

public class MySingletonMain {

	public static void main(String[] args) {
		/**객체를 new 하더라도 매번 객체가 만들어지지 않도록 할 경우 싱글톤 패턴을 이용한다
		 * (Gof 디자인 패턴 중 하나)**/
		
		MySingleton s1 = new MySingleton();
		MySingleton s2 = new MySingleton();
		System.out.println(s1 + " " + s2);
		//아직까지는 주소가 다름, 따로 new 했기 때문
		
		s1.kor = 80;
		s2.kor = 100;
		System.out.println(s1.kor + " " + s2.kor);
		System.out.println();
		
		MySingleton s3 = MySingleton.getInstance();
		MySingleton s4 = MySingleton.getInstance();
		//new를 안하고 객체를 생성, 내부적으로 new를 이용해 객체를 생성했기 때문
		System.out.println(s3 + " " + s4); //주소가 같음 = 같은 오브젝트 참조
		
		s3.kor = 88;
		System.out.println(s3.kor + " " + s4.kor); 
		//같은 것을 참조하기 때문에 값이 같음
	}

}
