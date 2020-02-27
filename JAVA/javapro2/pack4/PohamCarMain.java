package pack4;

public class PohamCarMain {
	
	public static void main(String[] args) {
		PohamCar tom = new PohamCar("톰");
		
		tom.turnHandle(30);
		System.out.println(tom.ownerName + "의 회전량은 " + tom.turnMessage + " " + tom.handle.quantity);
		//클래스의 포함관계
		
		tom.turnHandle(0);
		System.out.println(tom.ownerName + "의 회전량은 " + tom.turnMessage + " " + tom.handle.quantity);
		
		System.out.println();
		
		PohamCar kildong = new PohamCar("길동");
		kildong.turnHandle(-10);
		System.out.println(kildong.ownerName + "의 회전량은 " + kildong.turnMessage + " " + kildong.handle.quantity);
	}
}
