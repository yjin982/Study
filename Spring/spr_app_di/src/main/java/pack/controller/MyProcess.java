package pack.controller;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import pack.model1.MoneyInter;

public class MyProcess implements MyInter{
	private MoneyInter inter;
	private int re[];
	
	public MyProcess(MoneyInter inter) { //생성자 주입
		this.inter = inter;
	}
	
	public void inputMoney() {
		try {
			InputStreamReader reader = new InputStreamReader(System.in);
			BufferedReader breader = new BufferedReader(reader);
			
			int myMoney = 0;
			System.out.print("금액 입력 : ");
			myMoney = Integer.parseInt(breader.readLine());
			re = inter.calcMoney(myMoney);
			
		}catch (Exception e) {
			System.out.println("inputMoney err " + e);
		}
	}
	
	public void showResult() {
		/////.....자바에서 문자열 더하기는 속도를 저하시킴
		//String ss = "";
		//ss = "만원 : " + re[0] + "\n";
		//ss += "천원 : " + re[1] + "\n";
		//ss += "백원 : " + re[2] + "\n";
		/////...StringBuffer 혹은 StringBuilder 사용
		
		StringBuffer sb = new StringBuffer();
		sb.append("만원 : " + re[0] + "\n");
		sb.append("천원 : " + re[1] + "\n");
		sb.append("백원 : " + re[2] + "\n");
		sb.append("십원 : " + re[3] + "\n");
		sb.append("일원 : " + re[4] + "\n");
		System.out.println(sb.toString());
	}
}
