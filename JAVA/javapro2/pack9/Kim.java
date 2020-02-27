package pack9;

public class Kim extends Thread{ // 김씨 고객 - sinhanBank.java
	@Override
	public void run() {
		SinhanBankMain.myBank.saveMoney(5000);
		System.out.println("남편 예금 후 잔액 : " + SinhanBankMain.myBank.getMoney());
	}
}
