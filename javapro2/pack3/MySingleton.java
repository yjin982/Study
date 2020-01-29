package pack3;


public class MySingleton {
	int kor = 10;
	/*
	 * 
	 */
	
	private static MySingleton singleton = new MySingleton();
	public static MySingleton getInstance() {
		return singleton;
	}
	
	

}
