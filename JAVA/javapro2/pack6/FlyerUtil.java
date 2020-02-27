package pack6;

public class FlyerUtil {
	public static void show(Flyer f) {
		f.fly();
		System.out.println("Q : 동물인가요?   A : " + f.isAnimal());
	}
}
