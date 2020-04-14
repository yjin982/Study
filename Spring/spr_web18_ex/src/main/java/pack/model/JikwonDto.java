package pack.model;

import org.springframework.stereotype.Component;

@Component
public class JikwonDto {
	private String jikwon_no, jikwon_name, jikwon_jik, jikwon_go;

	public String getJikwon_no() {
		return jikwon_no;
	}

	public void setJikwon_no(String jikwon_no) {
		this.jikwon_no = jikwon_no;
	}

	public String getJikwon_name() {
		return jikwon_name;
	}

	public void setJikwon_name(String jikwon_name) {
		this.jikwon_name = jikwon_name;
	}

	public String getJikwon_jik() {
		return jikwon_jik;
	}

	public void setJikwon_jik(String jikwon_jik) {
		this.jikwon_jik = jikwon_jik;
	}

	public String getJikwon_go() {
		return jikwon_go;
	}

	public void setJikwon_go(String jikwon_go) {
		this.jikwon_go = jikwon_go;
	}
}
