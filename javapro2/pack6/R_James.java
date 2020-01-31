package pack6;

public class R_James implements Resume{
	private String irum, phone, skill;
	
	public R_James() {}
	
	@Override
	public void setIrum(String irum) {
		if(irum.equals(null))
			this.irum= "무명";
		else
			this.irum = irum;
	}
	@Override
	public void setPhone(String phone) {
		this.phone = phone;
	}
	public void setSkill(String skill) {
		this.skill = skill;
	}
	
	@Override
	public void print() {
		System.out.println("이력서 용지 규격은 " + Resume.SIZE);
		System.out.println("이름 : " + irum + ", 전화 : " + phone + ", 보유기술 : " + skill);
		playJava(true);
	}
	@Override
	public void playJava(boolean b) { //인터페이스의 default 메소드를 오버라이드
		Resume.super.playJava(b);
	}
}
