package pack6;

public interface Volume {
	/*일반 클래스에서 선언시
	 *public abstract void volumeUP(int level);  */
//	public void print() {		//일반 메소드 불가능		}
	
	void volumeUP(int level);
	void volumeDown(int level);
		
}
