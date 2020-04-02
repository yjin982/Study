package pack.required;

import org.springframework.beans.factory.annotation.Required;

public class Abc {
	private int number;
	
	@Required   //현재 setter에 반드시 값을 주도록 요구하는 어노테이션
	public void setNumber(int number) {
		this.number = number;
	}
	
	public String showData() {
		return "number : " + number;
	}
	
	
}
