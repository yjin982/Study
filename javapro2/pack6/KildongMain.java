package pack6;

public class KildongMain {
	public static void main(String[] args) {
		Saram saram = new Saram();
		System.out.println(saram.getIr());
		
		Kildong kildong = new Kildong();
		Saram saram2 = kildong.findSaram();
		System.out.println(saram2.getIr());
		
		
	}
}
