package pack.autowired;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Main {
	public static void main(String[] args) {
		String[] metas = new String[] {"anno2.xml"}; //meta 파일을 배열로 여러개 넣을 수 있음
		ApplicationContext context = new ClassPathXmlApplicationContext(metas);
		
		SenderProcess process = context.getBean("senderProcess", SenderProcess.class);
		process.dispData();   
		//process.getSender().show(); // dispData{ sender.show(); } 이니까 같은 말
		
		SenderProcess2 process2 = context.getBean("korea", SenderProcess2.class);
		process2.dispData();
		//process2.getInter().show();
		
		//SenderProcess process = context.getBean("aa", SenderProcess.class); ////@Component("aa")로 생성했으면 이렇게 불러주는것과 같음
		//process.dispData();   ///헷갈리기 때문에 비슷한 이름으로 지정하는 것이 좋음
		
	}
}
