package pack1;

import java.util.Scanner;

public class Test8 {

	public static void main(String[] args) {
		/*************switch***************/
		int age = 23;
		age = age / 10 * 10;
		
		switch (age) {
		case 10:
			System.out.println("십대");
			break;
		case 20:
			System.out.println("이십대");
			System.out.println("EE");
			break;
		case 30:
			System.out.println("삼십대");
			break;
		default:
			System.out.println("기타");
			break; //디폴트의 브레이크는 옵션
		}
		
		String jik = "과장";
		switch(jik) {//구버전은 문자열 안됐지만 이제 가능
		case "대리":
			System.out.println("대리");
			break;
		case "과장":
			System.out.println("과장");
			break;
		default:
			System.out.println("기타");
			break;
		}
		
		/*키보드로 년과 월을 입력받아 해당 년의 월 날 수 출력, 윤년체크
		 *윤년은 해당 년의 4의 배수이고 100의 배수가 아니거나 400의 배수이면 된다.
		 */
		int year, month, days = 28;
		Scanner sc = new Scanner(System.in);
		System.out.print("년도 입력: ");
		year = sc.nextInt();
		System.out.print("월 입력: ");
		month = sc.nextInt();
		
		if(month < 1 || month >12) {
			System.out.println("월은 1~12 사이만 허용");
			System.exit(1);
		}
		
		if(year % 4 == 0 && year % 100 != 0 || year % 400 == 0) {
			days = 29;
		}
		
		switch(month) {
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:
			days = 31;
			break;
		case 4:
		case 6:
		case 9:
		case 11:
			days = 30;
			break;
		}
		
		System.out.println(year + "년 " + month + "월 날수 :" + days);
		
	}

}
