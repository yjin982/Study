package pack;

public class Goods { //각 상품 정보를 담기 위한 DTO
	private String name;
	private int price;
	
	
	public Goods(String name, int price) {
		this.name = name;
		this.price = price;	
	}
	
	public String getName() {
		return name;
	}
	public int getPrice() {
		return price;
	}
}
