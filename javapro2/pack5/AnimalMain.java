package pack5;

public class AnimalMain {
	public static void main(String[] args) {
		AniCow cow = new AniCow();
		System.out.println(cow.callName() + "은(는) " + cow.action() + "에 " + cow.eat() + " 먹음");
		cow.print();
		
		AniLion lion = new AniLion();
		System.out.println("\n" + lion.callName() + "은(는) " + lion.action() + "에 " + lion.eat() + " 먹음");
		lion.print();
		lion.eatOther();
		
		System.out.println("ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ");
		
		AnimalFind.find(cow);
		AnimalFind.find(lion);
	}
}
