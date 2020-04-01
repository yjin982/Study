package pack.business;

public class DataFormBean {
	private String id, name, passwd;
	private String colname; //sql문 조건의 칼럼명을 동적으로 처리하기 위함
	
	
	public void setColname(String colname) {
		this.colname = colname;
	}
	public String getColname() {
		return colname;
	}

	public String getId() {
		return id;
	}

	public void setId(String id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getPasswd() {
		return passwd;
	}

	public void setPasswd(String passwd) {
		this.passwd = passwd;
	}
	
}
