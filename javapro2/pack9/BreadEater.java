package pack9;

public class BreadEater extends Thread{ 
	private BreadPlate plate;
	
	/**생성자**/
	public BreadEater(BreadPlate plate) {
		this.plate = plate;
	}
	
	/**메소드**/
	@Override
	public void run() {
		for (int i = 0; i < 30; i++) {
			plate.eatBread();
		}
	}
}
