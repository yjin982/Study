package pack;

public class Message1 implements MessageInter{
	
	public Message1() {
		//Init.xml 의 <bean id="mes">이 이 생성자와 같은 것(생성자에 인자를 넣으면 다르기때문에 xml에서 에러가 발생)
		System.out.println("생성자");
	}
	
	@Override
	public void sayHello(String name) {
		System.out.println("안녕 " + name + "씨");
	}
	
	
}
