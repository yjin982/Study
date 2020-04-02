package pack;

//핵심 로직 클래스
public class MessageImpl implements MessageInter{
	private String name;
	
	public void setName(String name) {
		this.name = name;
	}
	
	public void sayHi() {
		System.out.println("안녕하세요, " + name + "님! 비즈니스 로직을 처리 중입니다.");
	}
}
