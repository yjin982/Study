package pack3;

public class ProductMain {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Production p = new Production("Computer", 100);
		Production p2 = new Production();
		p.setProductionDay("2020-01-29");
		
		p2.display();
		p.display();
		p.display("TV");
		p.display("Phone", 90);

	}

}
