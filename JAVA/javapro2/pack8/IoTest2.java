package pack8;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.InputStreamReader;
import java.util.Scanner;

public class IoTest2 {
	public static void main(String[] args){
		//console을 통한 입력
		/////방법1
		try {
			InputStreamReader isr = new InputStreamReader(System.in);
			BufferedReader br = new BufferedReader(isr);
			System.out.print("이름 입력 : ");
			String ir = br.readLine();
			System.out.print("나이 입력 : ");
			String nai = br.readLine(); //int n = Integer.parseInt(br.readLine();
			System.out.println("이름:" + ir + "   나이:" + nai);
			br.close();
			isr.close();
		} catch (Exception e) {
			System.out.println("에러:" + e);
		}
		
		/////방법2 (방법1 주석처리하고 실행)
		try {
			Scanner sc = new Scanner(System.in);
			System.out.print("이름 입력 : ");
			String ir = sc.nextLine();
			System.out.print("나이 입력 : ");
			int nai = sc.nextInt(); //int n = Integer.parseInt(br.readLine();
			System.out.print("몸무게 입력 : ");
			double wei = sc.nextDouble();
			System.out.println("이름:" + ir + "   나이:" + nai + "   몸무게:" + wei);
			sc.close();
		} catch (Exception e) {
			System.out.println("에러:" + e);
		}
		
		
		try {
			//File fi = new File("c:/work/iotest.txt");			//FileReader fr = new FileReader(fi);
			FileReader fr = new FileReader(new File("c:/work/iotest.txt"));
			BufferedReader reader = new BufferedReader(fr);
			while(true) { //파일 읽기
				String ss = reader.readLine();
				if(ss == null) break;
				System.out.println(ss);
			}
			reader.close();
			fr.close();
		} catch (Exception e) {
			System.out.println("에러:" + e);
		}
		
	}
}
