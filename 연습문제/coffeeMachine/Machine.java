package aa.bb.pack4;

import java.util.Scanner;

public class Machine {
	private int cupCount = 0;
	private CoinIn c1= new CoinIn();
	
	public Machine() {}
	
	public void showData() {
		Scanner sc = new Scanner(System.in);
		
		System.out.print("동전을 입력하세요 : ");
		c1.setCoin(sc.nextInt());
		System.out.print("몇 잔을 원하세요 : ");
		this.cupCount = sc.nextInt();
		
		int jandon = c1.calc(this.cupCount);
		
		if(jandon < 0) System.out.println("요금이 부족합니다.");
		if(jandon >= 0) System.out.println("커피 " + this.cupCount +"잔과 잔돈 "+ jandon +"원");
		
		/**다른 방식
		 * System.out.println(c1.calc(this.cupCount));
		 * */
		sc.close();
	}
}
