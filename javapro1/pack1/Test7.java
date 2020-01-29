package pack1;

import java.util.Scanner;

public class Test7 {

	public static void main(String[] args) {
		/*************조건판단문 if***************/
		int num = 2;
		if (num >= 3) {
			System.out.print("크다 ");
			System.out.println("참일 때");
		}
		
		num = 5;
		if (num < 3) {
			System.out.print("작다 ");
			System.out.println("참이다");
		}else {
			System.out.print("크지 않다 ");
			System.out.println("거짓이다");
		}
		/*************다중if***************/
		int score = 80;
		if (score >= 70) {
			if(score >= 90)
				System.out.println("우수 ");
			else
				System.out.println("보통");
			
		}else{
			if(score >= 50)
				System.out.println("조금 부족");
			else
				System.out.println("저조");
		}
		/*************if else***************/
		int jum = 75;
		String result = "평가결과 : ";
		
		if(jum >= 90)
			result += "수";
		else if(jum >= 80)
			result += "우";
		else if(jum >= 70)
			result += "미";
		else if(jum >= 60)
			result += "양";
		else
			result += "가";
		System.out.println(result);
		
		/* 문제) 키보드로부터 상품명, 수량, 단가를 각각 입력받아
		 * 금액을 출력한다(금액 = 수량*단가)
		 * 조건 : 금액이 5만원 이상이면 금액에 10%를 그외는 금액의 5%를 세금으로 출력
		 * 출력 ==> 상품명:***     금액:***    세금:***
		 */
		
		String name;
		int dan, su, price;
		double tex;
		Scanner sc = new Scanner(System.in);
		
		System.out.print("상품명을 입력하세요: ");
		name = sc.next();
		System.out.print("수량을 입력하세요: ");
		su = sc.nextInt();
		System.out.print("단가을 입력하세요: ");
		dan = sc.nextInt();
		
		price = dan*su;
		
		if(price >= 50000)
			tex = price * 0.1;
		else
			tex = price* 0.05;
		
		System.out.println("상품명: " + name + " 가격: " + price + " 세금: " + tex);
		
		System.out.println("종료");

	}

}
