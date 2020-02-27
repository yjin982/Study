package pack5;

public abstract class Animal {
	
	public abstract String callName();
	public abstract String eat();
	public abstract String action();
	
	public void print() {
		System.out.println("동물 클래스의 print 일반 메소드");
	}
}
