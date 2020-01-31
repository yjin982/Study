package pack6;

public interface Resume {
	String SIZE = "A4"; // == public final static ...
	
	void setIrum(String irum);
	void setPhone(String phone);
	void print();
	
	/**인터페이스에서 default와 static 제한자를 써서 작성 가능하기는 하지만 흔한 경우가 아님**/
	default void playJava(boolean b) {
		if(b) {
			System.out.println("자바 프로그래밍 가능");
		}else {
			System.out.println("자바 불가능");
		}
	}	
	static void changeData() {
		System.out.println("스테틱 메소드 처리 가능");
	}
}
