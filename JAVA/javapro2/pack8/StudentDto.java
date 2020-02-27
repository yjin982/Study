package pack8;

public class StudentDto {
	private String hakbun, irum;
	private int jumsu;
	//타입이 다른 데이터를 하나의 묶음으로 처리
	
	
	/** get, set **/
	public int getJumsu() {
		return jumsu;
	}
	public void setJumsu(int jumsu) {
		this.jumsu = jumsu;
	}
	public String getHakbun() {
		return hakbun;
	}
	public void setHakbun(String hakbun) {
		this.hakbun = hakbun;
	}
	public String getIrum() {
		return irum;
	}
	public void setIrum(String irum) {
		this.irum = irum;
	}
}
