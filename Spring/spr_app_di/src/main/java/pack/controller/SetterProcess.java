package pack.controller;

import pack.model1.SetterShowData;

public class SetterProcess { //비즈니스 로직
	private int nai;
	private SetterShowData setterShowData;
	
	public SetterProcess() {}
	
	public void setNai(int nai) {
		this.nai = nai;
	}
	public void setSetterShowData(SetterShowData setterShowData) {
		this.setterShowData = setterShowData;
	}
	
	public void showData() {
		System.out.println("이름은 " + setterShowData.getName() + ", 나이는 " + nai + ", 취미는 " + setterShowData.getHobby());
	}
}
