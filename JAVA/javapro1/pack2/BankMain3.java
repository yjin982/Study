package pack2;
import pack3.Bank; //참조 라이브러리 안의 pack3.bank

public class BankMain3 {

	public static void main(String[] args) {
		/**다른 프로젝트의 클래스는 import 불가능
		 *  물리적으로 복사를 해야함 혹은
		 *  export해서 jar파일을 만들어서 build path에 jar파일을 추가 **/
		Bank joi = new Bank();
		System.out.println(joi.getMoney());

	}

}
