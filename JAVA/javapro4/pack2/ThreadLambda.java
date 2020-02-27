package pack2;

public class ThreadLambda {
	
	public ThreadLambda() {
		m1();
		m2();
		m3();
		m4();
	}
	
	public void sendEmail(String ss) {
		System.out.println(ss + " 메세지 전송");
	}
	
	void m1() { //전통적인 방법
		new Thread(new Runnable() {
			@Override
			public void run() {
				sendEmail("m1");
			}
		}).start();
	}
	void m2() {
		Thread thread = new Thread(() -> sendEmail("m2"));
		thread.start();
	}
	void m3() {
		new Thread(() -> sendEmail("m3")).start();
	}
	void m4() {
		Runnable runnable = () -> sendEmail("m4");
		runnable.run();
	}

	public static void main(String[] args) {
		new ThreadLambda();
	}
}
