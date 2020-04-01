package pack.order;

import java.util.Hashtable;

public class CartMgr {//장바구니는 db에 넣는게 아니라 램에 담아뒀다가 주문시에 db로 삽입
	private Hashtable hCart = new Hashtable();
	
	
	public void addCart(OrderBean obean) {//카트에 상품 추가하기
		String product_no = obean.getProduct_no();
		int quantity = Integer.parseInt(obean.getQuantity());
		
		if(quantity > 0) {
			
			if(hCart.containsKey(product_no)) {//동일 상품 주문시 주문 수량만 증가
				OrderBean temp = (OrderBean)hCart.get(product_no); //get은 꺼내기
				quantity += Integer.parseInt(temp.getQuantity()); //수량 누적
				temp.setQuantity(Integer.toString(quantity));
				hCart.put(product_no, temp);
				
			}else { //새 상품 주문인 경우
				hCart.put(product_no, obean); //put은 집어넣기
			}
		}
	}
	
	public void updateCart(OrderBean obean) { //카트 목록 수정
		String product_no = obean.getProduct_no();
		hCart.put(product_no, obean);
	}
	
	public void deleteCart(OrderBean obean) { //카트 목록 삭제
		String product_no = obean.getProduct_no();
		hCart.remove(product_no);
	}
	
	public Hashtable getCartList() {//카트 목록 가져오기
		
		return hCart;
	}
	
	
}
