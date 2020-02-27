package pack8;

import java.io.FileNotFoundException;
import java.io.FileReader;

/***예외처리 : 외부장치(키보드, 파일, DB, 네트워크 등)와 연결해 작업 시 반드시 기술을 해주어야 함. 그 외는 선택적으로 기술함.***/
public class TryTest {
	
	public void test() { //지역 문제 우선
		try {
			int a[] = {1,2,3};
			System.out.println("배열 값" + a[0]); //정상 코드
//			System.out.println("배열 값" + a[5]);
		} catch (Exception e) {
			System.out.println("허걱 에러 : " + e);
		}
	}
	
	/***** MAIN *****/
//	public static void main(String[] args) throws Exception { // throws Exception : 에러 처리하지 않고 던져버림
	public static void main(String[] args) {
//		FileReader fr = new FileReader("c:\\work\\aa.txt"); // 파일 경로는 \ , 혹은 / 둘다 가능함, \ 로 표시할 시 두 번 작성( 앞은 이스케이프 문자 )
		
		
		try { //try 안에서 에러가 발생하면 catch 에서 처리
			FileReader fr = new FileReader("c:/work/aa.txt"); 
						
			int re = 10 / 2; // java.lang.ArithmeticException 
			System.out.println("re : " + re);
			
			 /**이전 줄에서 에러가 있으면 이후 코드는 실행되지 않음**/
			TryTest tt = null; 
//			TryTest tt = new TryTest();
			tt.test();
			
		/*
		} catch (FileNotFoundException e) { //Exception의 서브클래스
			System.out.println("파일 오류");
		}catch (ArithmeticException e) { // 0으로 나눴을 경우에만 처리
			//e.printStackTrace(); // 에러 처리 방식은 선택적
			System.out.println("나누기 에러 : " + e.getMessage());			
		}catch (NullPointerException e){
			System.out.println("객체 오류 : " + e);
		}catch (ArrayIndexOutOfBoundsException e){
			System.out.println("배열 참조 오류 : " + e);
		}
		*/
		}catch(Exception e) {
			System.out.println("오류 : " + e);
		}
		
		System.out.println("종료");
	}
}
