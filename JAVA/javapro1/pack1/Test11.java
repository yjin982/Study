package pack1;

import java.util.Scanner;

public class Test11 {

	public static void main(String[] args) {
		/*************반복문 while***************/
//		int w = 1;
//		while(w <= 5) {
//			System.out.print("w:" + w  + " ");
//			w++;
//		}System.out.println("\n반복문 탈출 후 w:" + w);
//		System.out.println();
//		
//		w = 0;
//		while(true) {
//			++w;
//			if(w == 10) break;
//			if(w == 5) continue;
//			System.out.print("w:"+ w + " ");
//		}System.out.println();
//		
//		w = 10;
//		do {
//			System.out.print("w:"+ w + " ");
//			w++;
//		}while(w <= 5);
		
		/**문1) 1~100 사이의 숫자 중 3의 배수이나 2의 배수가 아닌 수를 출력하고
		 * 합과 갯수를 출력
		 */
		int w1 = 1, count = 0, sum = 0;
		while(w1<101) {
			if(w1 % 3 == 0 && w1 % 2 != 0) {
				System.out.print(w1 + " ");
				count++;
				sum += w1; 
			}
			w1++;
		}System.out.println("\n갯수:" + count + " 합:" + sum);
		System.out.println("________________________");
		
		/**문2) -1, 3, -5, 7, -9, 11 ~ 99까지의 합
		 */
//		야매
//		int sum2 = 0;
//		for (int i = 1, j = 3; i < 100; i += 4, j += 4) {
//			sum2 = sum2 + (i*-1) + j;
//			//System.out.print((i*-1) + " " + j + " ");
//		}
//		System.out.println("합:" + sum2);
		int flag = 1, sum2 = 0;
		for (int i = 1; i < 100; i += 2) {
			if(flag > 0) {
				sum2 -= i;
			}
			if(flag < 0){
				sum2 += i;
			}
			flag = -flag;
		}
		System.out.println(sum2);
		
		System.out.println("________________________");
		
		/**문3) 1 ~ 1000 사이의 소수와 그 갯수를 출력
		 * 소수 : 1보다 크고 1과 그 수 자체로만 나누어 떨어지는 수
		 * 방법1 - while
		 * 방법2 - for
		 */
		int count2 = 0;
		for(int i = 2; i <= 1000; i++) {
			for(int j = 2; j <= i; j++) {
				if (i == 2) {
					System.out.print(i + " ");
					count2++;
				}
				else if(i%j == 0) {
					if(i/j != 1) {
						break;
					}else{
						System.out.print(i + " ");
						count2++;
					}
				}
			}
			if(i % 100 == 0) System.out.println();
		}
		System.out.println("갯수:" + count2);
		
//		int count2=0, ss = 2;
//		
//		while(ss <= 1000) {
//			boolean s = false;
//			int kk = 2;
//			while(kk < ss) {
//				if( ss % kk == 0) {
//					s = true;
//				}
//				kk++;
//			}
//			if(s == false) {
//				count2++;
//			}
//			ss++;
//		}
//		System.out.println(count2);
		
		System.out.println("________________________");
		
		/**문4) 
		 * 		       AA
		 *           ABBA
		 *         ABCCBA
		 *       ABCDDCBA
		 *     ABCDEEDCBA
		 *      ABCDDCBA     
		 *        ABCCBA
		 *          ABBA        
		 *            AA
		 */
		int start = 'A', last = 'E';
		
		for (int i=start; i<=last; i++) {
			for (int j=i; j<=last; j++) {
				System.out.print("  ");
			}
			for (int j=start; j<=i; j++) {
				System.out.print((char)j);
			}
			for (int j=i; j>=start; j--) {
				System.out.print((char)j);
			}
			System.out.println();
		}
		for (int i=last-1; i>=start; i--) {
			for (int j=i; j<=last; j++ ) {
				System.out.print("  ");
			}
			for (int j=start; j<=i; j++) {
				System.out.print((char)j);
			}
			for (int j=i; j>=start; j--) {
				System.out.print((char)j);
			}
			System.out.println();
		}
		
//		for (int a = 5; a >= -5; a--) {
//			if (a != 0) {
//				int atemp = 0;
//				if (a < 0)
//					atemp = a * -1;
//				else
//					atemp = a;
//
//				for(int b = 1; b < atemp; b++) {
//					System.out.print("  ");
//				}
//
//				for(int c = 1; c <= 6 - atemp; c++) {
//					char ch = 'A';
//					System.out.print((char)(ch + c - 1));
//				}
//				
//				for(int c = atemp; c <= 5; c++) {
//					char ch = 'E';
//					System.out.print((char)(ch - (c - 1)));
//				}
//				System.out.println();
//			}
//		}
		System.out.println("________________________");
		
		/**문5) 키보드로 숫자 입력 : 5
		 * 그러면 5까지의 합 출력
		 * 계속할까요? (y/n) 묻게 하고 y면 다시 키보드로 정수받아 합 출력하고 n이면 탈출
		 */
		Scanner sc = new Scanner(System.in);
		int w5 = 0, sum5 = 0;
		char q = 'y';
		while(true) {
			System.out.print("키보드로 숫자 입력: ");
			w5 = sc.nextInt();
			for(int i=1; i<=w5; i++) {
				sum5 += i;
			}
			System.out.println("합:" + sum5);
			System.out.print("계속할까요? (y/n)  ");
			q = sc.next().charAt(0);
			if(q == 'n') {
				break;
			}else{
				sum5 = 0;
			}			
		}
		
		
	}

}
