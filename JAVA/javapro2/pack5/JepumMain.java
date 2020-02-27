package pack5;

public class JepumMain {
	public static void main(String[] args) {
		//Jepum jepum = new Jepum(); //추상 클래스이므로 에러
		
		Jepum jepum = null;
		
		Jepum_Tv tv = new Jepum_Tv();
		jepum = tv;
		jepum.volumeControl();
		
		System.out.println();
		
		Jepum_Radio radio = new Jepum_Radio();
		jepum = radio;
		jepum.volumeControl();
	}
}
