package pack5;

public class AniCow extends Animal{
	
	@Override //어노테이션 = meta
	public String action() {
		return "낮";
	}
	@Override
	public String callName() {
		return "소";
	}@Override
	public String eat() {
		return "여물";
	}
}
