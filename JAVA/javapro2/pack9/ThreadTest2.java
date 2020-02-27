package pack9;

public class ThreadTest2 implements Runnable{
	
	public ThreadTest2() {}
	public ThreadTest2(String name) {
		Thread tt = new Thread(this, name);
		tt.start(); 
	}
	
	
	@Override
	public void run() {
		for (int i = 0; i < 20; i++) {
			System.out.print(i + "[" + Thread.currentThread().getName() + "] ");
		}
		System.out.println();
	}
	
	public static void main(String[] args) {
		/* Runnable 인터페이스를 상속받아서 스레드 실행
		ThreadTest2 my1 = new ThreadTest2();
		ThreadTest2 my2 = new ThreadTest2();
//		my1.start();  // X 
		Thread t1 = new Thread(my1, "원");
		Thread t2 = new Thread(my2);
		t1.start();
		t2.start();
		*/
		
		/* 생성자에서 스레드 시작 */
		new ThreadTest2("one");
		new ThreadTest2("two");
		
		System.out.println("프로그램 종료");
	}
}
