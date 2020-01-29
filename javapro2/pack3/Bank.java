package pack3;

public class Bank {
	private int money = 1000;
	int imsi = 1;
	public int imsi2 = 2;
	
	public Bank() {}
	public Bank(int money) {   this.money += money;   }
	
	
	public int getMoney() {   return money;    }
	
	
	public void dePosit(int amount) { //입금
		if(amount > 0) money += amount;
	}
	public void withDraw(int amount) { //출금
		if((amount > 0) && (money - amount >= 0)) money -= amount;
		else	System.out.println("출금액이 너무 많아요");
	}
	
	/**관련 파일
	 * javapro2.pack3.BankMain.java
	 * javapro2.etc_pack.BankMain2.java
	 * javapro1.pack2.BankMain3.java********/
}
