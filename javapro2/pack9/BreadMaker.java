package pack9;

public class BreadMaker extends Thread{ 
	private BreadPlate plate;
	
	/**생성자**/
	public BreadMaker(BreadPlate plate) {
		this.plate = plate;
	}
	
	/**메소드**/
	@Override
	public void run() {
		for (int i = 0; i < 30; i++) {
			plate.makeBread();
		}
	}
}
