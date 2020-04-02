package pack;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import other.OutFileImpl;

@Configuration  //arrange.xml 대신 클래스에 어노테이션을 적용
public class Config {
	
	@Bean  //xml에서 <bean>, 객체 생성
	public MyInfo myInfo() {
		return new MyInfo();
	}
	
	@Bean(name="messageImpl") //messageImpl 라는 이름으로 객체 생성
	public MessageImpl messageImpl() {
		MessageImpl impl = new MessageImpl("장비", "관우", 2100, myInfo());
		impl.setSpec("파이썬 선수 예정");
		impl.setMyInfo2(myInfo());
		impl.setFileInter(fileImpl());
		return impl;
	}
	
	@Bean
	public OutFileImpl fileImpl() {
		OutFileImpl fileImpl = new OutFileImpl();
		fileImpl.setFilePath("c:/work/omygod.txt");
		return fileImpl;
	}
}
