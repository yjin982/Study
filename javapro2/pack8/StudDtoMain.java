package pack8;

import java.util.ArrayList;
import java.util.Scanner;

public class StudDtoMain {
	ArrayList<StudDto> list = new ArrayList<StudDto>();
	
	
	public void insertData() {
		Scanner sc = new Scanner(System.in);
		StudDto sd = null;
		String flag = "y";
		
		while(flag.equals("y")) {
			sd = new StudDto();
			
			System.out.print("이름 입력 : ");
			sd.setName(sc.next());
			System.out.print("국어 점수 : ");
			sd.setKor(sc.nextInt());
			System.out.print("영어 점수 : ");
			sd.setEng(sc.nextInt());
			list.add(sd);
			
			System.out.print("계속 할까요? (y/n) ");
			flag = sc.next();
			if(flag.equals("n")) {
				System.out.println("입력을 종료합니다.\n");
			}else if(flag.equals("y")) {
				continue;
			} else {
				System.out.print("y 혹은 n만 입력하세요 : "); 
				flag = sc.next();
			}
		}
	}
	
	public void showData() {
		int total = 0;
		
		System.out.println("\n이름 \t국어  \t영어  \t총점");
		for(StudDto sd:list) {
			total = sd.getEng() + sd.getKor();
			System.out.println(sd.getName() + " \t" + sd.getKor() + "  \t" + sd.getEng() + "  \t" + total);
			
		}
		System.out.println("응시 인원   " + list.size() + "명");
		
	}
	
	
	public static void main(String[] args) {
		StudDtoMain sd = new StudDtoMain();
		
		sd.insertData();
		sd.showData();
	}
}
