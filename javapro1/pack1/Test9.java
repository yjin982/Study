package pack1;

import java.util.Scanner;

public class Test9 {

	public static void main(String[] args) {
		/*************반복문 for***************/
//		int a;
//		int sum = 0;
//		for(a=1; a<=10; a++) {//초기치;조건;증감치 {수행문 ... }
//			System.out.print(a + "  ");
//			sum += a;
//		}
//		System.out.println("\nfor 탈출 후 a값 " + a);
//		System.out.println("합은: " + sum);
//		
//		for(int i = 65; i < 91; i++) {
//			System.out.print((char)i + "\t");
//		}System.out.println();
//		for (int i = 'A'; i <= 'Z'; i++) {
//			System.out.print(i + "\t");
//		}System.out.println();
//		
//		for (int i = 10; i > 1; i -= 2) {
//			System.out.print(i + "\t");
//		}System.out.println();
//		
//		for (int i = 0, j = 5; i <= 5; i++,j++) {
//			System.out.println("i: " + i + "  j: " + j);
//		}
//		
//		int aa = 1;
//		for(;aa<= 5; aa++) {
//			System.out.print(aa + "\t");
//		}System.out.println();
		
		/**문제1) 키보드로부터 숫자를 입력받아 (2~9사이만 허용) 구구단 출력
		 * ex) 2 * 1 = 2 ... 
		 * */
		Scanner sc = new Scanner(System.in);
		int num;
		boolean b = false;
		System.out.print("숫자 입력: ");
		num = sc.nextInt();
		
		if(num < 2 || num > 9) {
			System.out.println("숫자는 2~9 사이만 허용입니다. ");
		}else{
			for (int i = 1; i < 10; i++) {
				System.out.println(num + " * " + i + " = " + num*i);
			}
		}
		
//		do {
//			if(num < 2 || num > 9) {
//				System.out.print("숫자는 2~9 사이만 허용입니다. 숫자 입력: ");
//				num = sc.nextInt();
//			}else {
//				b = true;
//				for (int i = 1; i < 10; i++) {
//					System.out.println(num + " * " + i + " = " + num*i);
//				}
//			}
//		}while(b == false);
		
		/**문제2) 1 ~ 100 사이의 숫자 중 3의 배수이면서 5의 배수의 갯수와 그들의 합은?
		 * */
		int count = 0, sum2 = 0;
		for(int i = 1; i <= 100; i++) {
			if(i % 3 == 0 && i % 5 ==0) {
				count++;
				sum2 += i;
			}
		}
		System.out.println("갯수:" + count + "   합:" + sum2);
		
		
	}

}
