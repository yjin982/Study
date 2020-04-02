package pack.model1;

public class MoneyCalc implements MoneyInter{
	
	public int[] calcMoney(int money) { //ex: 12345가 들어왔다면
		int re[] = new int[5];
		re[0] = money / 10000;
		re[1] = money % 10000 / 1000;
		re[2] = money % 10000 % 1000 / 100;
		re[3] = money % 10000 % 1000 % 100 / 10;
		re[4] = money % 10000 % 1000 % 100 % 10;
		return re;
	}
	public void dispMoney() {
		
	}
}
