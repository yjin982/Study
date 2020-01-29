package aa.bb.pack4;

public class PohamHandle {
	int quantity;   	//회전량

	public PohamHandle() {
		quantity = 0;
	}

	
	String leftTurn(int quantitiy) {
		this.quantity = quantitiy;
		return "좌회전";
	}
	String rightTurn(int quantitiy) {
		this.quantity = quantitiy;
		return "우회전";
	}
	String straight(int quantitiy) {
		this.quantity = quantitiy;
		return "직진";
	}
	
}
