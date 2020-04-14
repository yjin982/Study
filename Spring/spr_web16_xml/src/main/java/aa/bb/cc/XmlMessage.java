package aa.bb.cc;

import javax.xml.bind.annotation.XmlAccessType;
import javax.xml.bind.annotation.XmlAccessorType;

@XmlAccessorType(XmlAccessType.FIELD)
public class XmlMessage { //xml 처리를 위한 DTO
	private String name;
	private String age;
	
	
	public XmlMessage(String name, String age) {
		this.name = name;
		this.age = age;
	}
	
	public String getName() {
		return name;
	}
	
	public String getAge() {
		return age;
	}
}
