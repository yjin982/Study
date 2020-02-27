package pack3;

/**method overloading : 동일한 이름의 메소드를 여러개 선언 가능. 단, 조건 필요**/
public class Animal {
	private int leg = 4;
	private int age;
	private String name;
	public final static int MOUTH = 1;
	
	public Animal() {		/*생성자는 내용이 없을 경우 생략이 가능, 컴파일러가 생성 */		}
	public Animal(int leg) {//생성자 오버로딩
		this.leg = leg;
	}
	public Animal(String name) {
		this.name = name;
	}
	
	public void display() {
		System.out.println("leg:" + leg + ", age:" + age + ", name:" + name);
	}
	public void display(int age) { 					//인자의 갯수가 다름
		this.age = age;
		System.out.println("leg:" + leg + ", age:" + age + ", name:" + name);
	}
	public void display(String name) { 			//갯수는 같으나 인자의 타입이 다름 
		this.name = name;
		System.out.println("leg:" + leg + ", age:" + age + ", name:" + name);
	}
	public void display(String name, int age) { //갯수도 인자의 타입도 다름 
		this.name = name;
		this.age = age;
		System.out.println("leg:" + leg + ", age:" + age + ", name:" + name);
	}
	public void display(int age, String name) { //갯수도 인자의 타입도 같으나, 위치가 다름
		this.name = name;
		this.age = age;
		System.out.println("leg:" + leg + ", age:" + age + ", name:" + name);
	}
	
	
	
}
