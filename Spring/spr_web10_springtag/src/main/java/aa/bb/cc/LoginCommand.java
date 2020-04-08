package aa.bb.cc;

import org.springframework.stereotype.Component;

@Component
public class LoginCommand {//login form과 연결되는 폼빈
	private String userid, passwd;

	public String getUserid() {
		return userid;
	}

	public void setUserid(String userid) {
		this.userid = userid;
	}

	public String getPasswd() {
		return passwd;
	}

	public void setPasswd(String passwd) {
		this.passwd = passwd;
	}
}
