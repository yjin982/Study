package etc_pack;
import pack3.Bank;

public class BankMain2 {

	public static void main(String[] args) {
		/** Bank 클래스 패키지와 다른 패키지에서 Bank 클래스를 호출 **/
		Bank john = new Bank();
//		System.out.println(john.imsi);   //default
		System.out.println(john.imsi2); //public
		System.out.println(john.getMoney());
		
		
		
		
	}

}
