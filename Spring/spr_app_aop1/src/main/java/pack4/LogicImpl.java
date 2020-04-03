package pack4;

import org.springframework.stereotype.Service;

@Service
public class LogicImpl implements LogicInter{
	
	public LogicImpl() {}
	
	public void startProcess() {
		System.out.println("검증이 됐으므로 핵심 로직 수행함");
	}
}
