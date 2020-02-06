package pack8;

import java.util.ArrayList;
import java.util.Scanner;
import java.util.StringTokenizer;

public class DtoProductMain {
	ArrayList<DtoProduct> list = new ArrayList<DtoProduct>();
	
	
	public void insertData() {
		Scanner sc = new Scanner(System.in);
		DtoProduct dp = null;
		String temp = "";
		String flag = "y";
		
		while(flag.equals("y")) {
			System.out.print(">> ");
			dp = new DtoProduct();
			StringTokenizer to = new StringTokenizer(sc.next(), ",");
			
			/*//지역 구분을 String으로 둔 경우
			temp = to.nextToken();
			if(temp.equals("100")) {
				dp.setArea("강북");
			}else if(temp.equals("200")) {
				dp.setArea("강남");
			}else if(temp.equals("300")) {
				dp.setArea("강서");
			}else {
				dp.setArea("기타");
			} */
			
			dp.setArea(Integer.parseInt(to.nextToken()));
			dp.setProductName(to.nextToken());              //상품명
			dp.setNum(Integer.parseInt(to.nextToken())); //수량
			list.add(dp);
			
			while(true) {
				System.out.print("계속 하시겠습니까? (y/n)  ");
				flag = sc.next();
				if(flag.equals("y") || flag.equals("n")){
					break;
				} else{
					System.out.println("y 혹은 n을 입력해주세요.");
					continue;
				}
			}
		}
	}
	
	public void showData() {
		int countP = 0, countS = 0;
		int total = 0, soP = 0, soS = 0;
		
		System.out.println("지역\t상품명\t수량\t단가\t금액");
		for(DtoProduct dp:list) { 
			
			//지역 구분
			if(dp.getArea() == 100) {
				System.out.print("강북\t");
			}else if(dp.getArea() == 200) {
				System.out.print("강남\t");
			}else if(dp.getArea() == 300) {
				System.out.print("강서\t");
			}else {
				System.out.print("기타\t");
			}
			
			//상품명에따라 소계 건수와 금액 계산
			if(dp.getProductName().equals("새우깡")) {
				countS++;
				soS += dp.getNum()*450;
				
				System.out.println(dp.getProductName() +"\t" 
						+ dp.getNum() +"\t" 
						+ "450\t"
						+ dp.getNum()*450);
				
			}else if(dp.getProductName().equals("감자깡")) {
				countP++;
				soP += dp.getNum() * 300;
				
				System.out.println(dp.getProductName() +"\t" 
						+ dp.getNum() +"\t" 
						+ "300\t"
						+ dp.getNum()*300);
			}
		}
		
		total = soP + soS;
		System.out.println("\n소계\t감자깡:" + countP + "\t소계액:" + soP + "원\n"
								 	    +"\t새우깡:" + countS + "\t소계액:" + soS + "원\n");
		System.out.println("총 건수: " + list.size() + "\t총액:" + total);
	}
	
	public static void main(String[] args) {
		DtoProductMain dpm = new DtoProductMain();
		
		System.out.println("입력 예시 : 지역코드,새우깡,수량");
		dpm.insertData();
		dpm.showData();
	}
}
