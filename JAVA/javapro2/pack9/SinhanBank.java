package pack9;

public class SinhanBank {
	private int money = 10000;   // 통장 잔고, 스레드의 공유 자원용
	
	
	public int getMoney() {
		return money;
	}
	public void setMoney(int money) {
		this.money = money;
	}
	
	
	/**메소드**/
	public synchronized  void saveMoney(int save) {    // 입금
		int m = getMoney();
		
		try { // 동기화 테스트를 위해 추가
			Thread.sleep(2000); 
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		setMoney(m + save);
	}
	public synchronized void minusMoney(int mon) {  // 출금
		int m = getMoney();
		
		try { // 동기화 테스트를 위해 추가
			Thread.sleep(3000); 
		}catch (Exception e) {
			e.printStackTrace();
		}
		
		setMoney(m - mon);
	}
}
