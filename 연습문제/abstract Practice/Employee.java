package pack4;

public abstract class Employee {
	private String irum = "";
	private int nai = 0;
	
	public Employee() {}
	public Employee(String irum, int nai) {
		this.irum = irum;
		this.nai = nai;
	}
	
	public abstract double pay();
	public abstract void print();
	
	public void display() {
		System.out.print("이름 : " + irum + "   나이 : " + nai + "  |  ");
	}
}
