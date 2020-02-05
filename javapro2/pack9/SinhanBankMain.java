package pack9;

public class SinhanBankMain {
	public static SinhanBank myBank = new SinhanBank();
	
	public static void main(String[] args) {
		//김씨와 아내가 신한은행에 공동계좌가 있다고 가정, 남편은 입금, 아내는 출금을 동시에 할 경우 공동자원인 money 상태는?
		System.out.println("초기 예금액:" + myBank.getMoney());
		Kim kim = new Kim();
		KimWife wife = new KimWife();
		kim.start();
		wife.start(); // 기본적으로 스레드는 자원 공유 하지 않는다. 자원 공유 하려면 동기화를 시켜야함. -> 메소드에 synchronized 
	}
}
