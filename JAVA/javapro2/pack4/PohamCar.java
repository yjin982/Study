package pack4;

public class PohamCar { //여러개의 부품(클래스)들을 조립해 완성차를 만드는 클래스
	int speed = 0;
	String ownerName, turnMessage;
	PohamHandle handle;   				//클래스의 포함(has a 관계)
	
	public PohamCar(String name) {
		this.ownerName = name;
		this.handle = new PohamHandle();
	}
	
	void turnHandle (int q) { //양수=우회전, 음수=좌회전, 0=직진 으로 가정
		if(q > 0) turnMessage = handle.rightTurn(q);
		if(q < 0) turnMessage = handle.leftTurn(q);
		if(q == 0) turnMessage = handle.straight(q);
	}
	
	

}
