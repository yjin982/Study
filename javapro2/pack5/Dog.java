package pack5;

public class Dog {//개과의 동물들이 가져야할 기본 멤버
	//멤버 변수
	private String name = "개";
		
	//생성자
	public Dog() {	}
	public Dog(String name) {
		this.name = name;
	}
	
	//메소드
	public String callName() {
		return "종류 : " + name;
	}
	public void print() {
		System.out.println(name + " : 한국에 살고 있다.");
	}
	
	//get,set
	public String getName() {
		return name;
	}
}
