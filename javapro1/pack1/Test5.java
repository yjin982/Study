package pack1;

import java.math.BigDecimal;

public class Test5 {

	public static void main(String[] args) {
		// BigDecimal
		double a = 2.0;
		double b = 1.1;
		System.out.println(a+b);
		System.out.println(a-b);
		System.out.println();
		/***************************************/
		BigDecimal d1 = new BigDecimal("2.0");
		BigDecimal d2 = new BigDecimal("1.1");
		System.out.println(d1.subtract(d2));
		System.out.println();
		/***************************************/
//		long aa = 12345678901234567890L;
		BigDecimal no1 = new BigDecimal("12345678901234567890");
		BigDecimal no2 = new BigDecimal("12345678901234567890");
		System.out.println(no1.add(no2));
		System.out.println();
	}

}
