package pack6;

public class Kildong {
//	public Saram findSaram() {
//		return new Saram();
//	}
	
	public Saram findSaram() {
		return new Saram()
		{//익명(무명) 클래스
			int abc = 0;
			public void aa() {
				System.out.println("익명 클래스의 aa 메소드");
				//익명클래스 자체의 메소드는 따로 부를 일이 없음 = 이름이 없으니까
				//오버라이드 메소드에서 사용하면서 부를 수 있음
			}
			
			public String getIr() {//Saram.java에 있던 메소드를 오버라이드
				String name = "홍길동";
				return name;
			}
		};
	}
}
