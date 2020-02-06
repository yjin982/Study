package pack4;

public class Salesman extends Regular{
	private int sales = 0;
	private double commission = 0.0;
	
	public Salesman() {}
	public Salesman(String irum, int nai, int salary, int sales, double commission) {
		super(irum,nai,salary);
		this.sales = sales;
		this.commission = commission;
	}
	
	@Override
	public double pay() {
		return super.pay() + (sales * commission);
	}
	@Override
	public void print() {
		display();
		System.out.println("수령액 : " + this.pay());
	}
}
