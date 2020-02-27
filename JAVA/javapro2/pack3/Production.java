package pack3;

public class Production {
	private String name;
	private int price;
	private String productionDay;
	
	
	public Production() {
		name = "default";
		price = 12345;
	}
	public Production(String name, int price) {
		this.name = name;
		this.price = price;
	}
	
	
	public void setProductionDay(String day) {
		this.productionDay = day;
	}
	
	
	public void display() {
		System.out.println("상품명: " +name+ ", 가격:" +price+ ", 생산일:" + productionDay);
	}
	public void display(String name) {
		System.out.println("상품명: " +name+ ", 가격:" +price+ ", 생산일:" + productionDay);
	}
	public void display(String name, int price) {
		System.out.println("상품명: " +name+ ", 가격:" +price+ ", 생산일:" + productionDay);
	}

}
