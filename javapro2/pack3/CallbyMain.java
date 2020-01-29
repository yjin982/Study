package pack3;

public class CallbyMain {

	public static void main(String[] args) {
		/**메소드 호출시 매개변수 전달**/
		Callby1 my = new Callby1();
		Callby2 your = new Callby2();
		
		System.out.println("원래          a:" +my.a+ ", b:" +my.b);
		System.out.println();
		
		your.ex(my.a, my.b);
		System.out.println("1. 수행 후  a:" +my.a+ ", b:" +my.b);
		System.out.println();
		
		your.ex(my);
		System.out.println("2. 수행 후  a:" +my.a+ ", b:" +my.b);
		System.out.println();
		
		System.out.println("원래          c[0]:" +my.c[0]+ ", c[1]:" +my.c[1]);
		your.ex(my.c);
		System.out.println("3. 수행 후  c[0]:" +my.c[0]+ ", c[1]:" +my.c[1]);
	}

}
