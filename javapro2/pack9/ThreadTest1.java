package pack9;

public class ThreadTest1 extends Thread{
	
	public ThreadTest1() {}
	public ThreadTest1(String name) {
		super(name);
	}
	
	@Override
	public void run() { // run 에서만 thread 호출 가능
		for (int i = 0; i < 20; i++) {
//			System.out.print(i + " ");
			System.out.print(i + "[" + super.getName() + "] "); // 어느 스레드가 실행되는지 이름을 받아서 출력해보기
			try {
				Thread.sleep(100); // 한번 강제로 재운 후 다시 프린트 (ms 단위 1000 = 1초)
			} catch (InterruptedException e) {
				e.printStackTrace();
			}
		}
		System.out.println();
	}
	
	public static void main(String[] args) { //Main(=Demon) thread에 의해 main() 수행
		
		try {
			/////process 단위 수행
//			Process p1 = Runtime.getRuntime().exec("calc.exe");        // 계산기 실행
//			Process p2 = Runtime.getRuntime().exec("notepad.exe");  // 메모장
			
//			p1.waitFor(); // 자신은 정상종료, 다른 프로세스는 비정상 종료
//			p2.destroy(); // kill the process
			
			
			///// thread 메소드 단위 수행
			/*
			ThreadTest1 t1 = new ThreadTest1();
			ThreadTest1 t2 = new ThreadTest1();
			t1.run(); // 단순히 메소드 실행
			System.out.println();
			t2.run(); // 단순 메소드이므로 t1의 0~50까지 프린트한 후에 t2가 0~50까지 프린트
			*/
			
			/*
			ThreadTest1 t1 = new ThreadTest1();
			ThreadTest1 t2 = new ThreadTest1();
			t1.start(); // 스레드를 실행시키기
			t2.start();
			*/
			
			ThreadTest1 t1 = new ThreadTest1("원");
			ThreadTest1 t2 = new ThreadTest1("투");
			t1.start();
			t2.start();
			t2.setPriority(MAX_PRIORITY); // 1~10까지 가능, MAX_PRIORITY=10 / MIN_PRIORITY=1 / 요청한다고 반드시 먼저 실행되는 것이 아님, 확률적으로 높은 우선순위
			t1.join(); // 사용자 스레드가 종료될 때까지 메인 스레드를 대기시킴
			t2.join();
			
			System.out.println("프로그램 종료"); // Demon 스레드가 수행하는 문장
						
		}catch (Exception e) {
			System.out.println("   ...   ...   " + e);
		}
		
		
	}
}
