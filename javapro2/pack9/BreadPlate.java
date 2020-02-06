package pack9;

public class BreadPlate {
	private int breadCount = 0; // 공유 자원
	
	
	/**생성자**/
	public BreadPlate() {}
	
	
	/**메소드 : 일반**/
	public synchronized void makeBread() {
		if(breadCount >= 10) {
			try {
				System.out.println("\t빵 생산 초과");
				wait(); // 빵이 10개 이상이면 스레드 비활성화
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
		breadCount++;  // 빵 생산
		System.out.println("빵 생산 후 갯수:" + breadCount + "개*");
		
		notify(); // 스레드 활성화 (wait() 해제)
	}
	public synchronized void eatBread() {
		if(breadCount < 1) {
			try {
				System.out.println("\t빵이 없어 대기");
				wait();
			}catch (Exception e) {
				e.printStackTrace();
			}
		}
		breadCount--;  // 빵 소비
		System.out.println("빵 소비 후 갯수:" + breadCount + "개");
		
		notify();
	}
}
