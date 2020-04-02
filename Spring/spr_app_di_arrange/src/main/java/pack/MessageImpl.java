package pack;

import other.OutFileInter;

public class MessageImpl implements MessageInter{
	/////생성자용
	private String name1, name2;
	private int year;
	private MyInfo myInfo;
	
	/////프로퍼티용
	private String spec;
	private MyInfo myInfo2;
	private OutFileInter fileInter; //외부 패키지클래스
	
	public MessageImpl(String name1, String name2, int year, MyInfo myInfo) { 
		//생성자 주입
		this.name1 = name1;
		this.name2 = name2;
		this.year = year;
		this.myInfo = myInfo;
	}
	
	// Setter 주입
	public void setSpec(String spec) {
		this.spec = spec;
	}
	public void setMyInfo2(MyInfo myInfo2) { //생성자로 주입도, setter로 주입하는 것도 가능(구분하기 쉬우라고 2를 추가작성)
		this.myInfo2 = myInfo2;
	}
	public void setFileInter(OutFileInter fileInter) {
		this.fileInter = fileInter;
	}
	
	public void sayHi() {
		//출력 담당
		String msg = name1 + " " + name2;
		msg += "\n" + (year + 20) + "년"; //year 2000만 가져올 것임
		msg += "\n" + myInfo.myData() + "  2|" + myInfo2.myData();
		msg += "\n스펙은 " + spec;
		System.out.println(msg);
		
		/////메세지를 파일로 출력////////////
		fileInter.outFile(msg); //메세지를 출력하기 위해서는 setter를 통해서 파일 주소를 밀어넣어주어야 한다
	}
}
