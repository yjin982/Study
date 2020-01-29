package pack3; //패키지명 : 성격이 비슷한 클래스들을 저장한 폴더명

//접근지정자 public, protected, default, private
public class Car { //접근지정자 class 클래스명(=대문자로 시작, source파일명과 일치)
	/**멤버필드(=전역 변수) : 속성(특성, 구성 요소)**/
	int wheel;						// 생략 == default : 현재 "패키지" 내에서 호출 가능
	private int airBag = 1; 	// private : 캡슐화(현재 "클래스" 내에서만 호출 가능)
	private int speed;			// 전역변수 초기화 필요x, 지역변수는 초기화 필요
	public String name;			// public : 현재 "프로젝트"에서 호출 가능 
	
	
	/**생성자 : 특별한 메소드로 객체 생성시 초기화를 담당 **/
	public Car() {//클래스와 이름이 같고, 반환형이 없음, 한 번만 부름(생성시에  new), 생략가능
		System.out.println("Car 생성자");
		speed = 10;
		name = "홍길동";
	}
	
	
	
	/**멤버 메소드**/ //접근지정자 반환형 메소드명(인수...)
	public void abc(){ 
		System.out.println("abc 수행 : speed => " + speed);
		abc2();
		String result = abc3(7);
		System.out.println("result : " + result);
	}
	private void abc2(){
		System.out.println("abc2 수행");
	}
	String abc3(int num){ //인자(인자, 매개변수, argument, parameter)가 있는 메소드
		int local = num + 3;		//지역변수 : 초기화 필요
		System.out.println("abc3 수행,  num : " + num);
		return "반환된 값은 " + (local * 10);
	}



	
	public void showAirBag() {
		System.out.println("airBag : " + airBag);
	}
	public int getAirBag() { //private 멤버 변수 처리용(출력) getter
		return airBag;
	}



	public void setAirBag(int pwd, int airBag) { //private 멤버 변수값 주입용(입력) setter
		if (pwd == 123) {
			this.airBag = airBag;
		}
	}
	

}
