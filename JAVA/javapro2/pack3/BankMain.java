package pack3;

public class BankMain {

	public static void main(String[] args) {
		//작업
		
		Bank tom = new Bank();
		tom.dePosit(5000);
		tom.withDraw(3000);
		System.out.println("tom의 잔고 : " + tom.getMoney() + "\n");
				
		
		Bank oscar = new Bank(3000);
		oscar.dePosit(1000);
		oscar.withDraw(7000);
		oscar.withDraw(4000);
		System.out.println("oscar의 잔고 : " + oscar.getMoney() + "\n------");
		
		/**주소 관련**/
		System.out.println("tom    주소 : " + tom);
		System.out.println("oscar  주소 : " + oscar.toString());   //hex
		System.out.println("oscar  주소 : " + oscar.hashCode());//decimal
		
		Bank james = null;
		System.out.println("james 주소 : " + james);
//		james.dePosit(2000); //NullPointerException
		System.out.println();
		
		james = oscar;
		System.out.println("james  주소 : " + james);
		james.dePosit(2000);
		System.out.println("james의 잔고 : " + james.getMoney());
		System.out.println("oscar의 잔고 : " + oscar.getMoney() + "\n");
//		oscar = null; //oscar는 null이 됐지만 james가 참조중이므로 객체 소멸x
		
		if(james == oscar) System.out.println("둘은 같은 객체 주소 참조");
		else System.out.println("달라요");
		
		if(james == tom) System.out.println("둘은 같은 객체 주소 참조2");
		else System.out.println("달라요2");
		
		
		System.out.println("\nString 클래스 타입값 비교");
		String ss1 = "kor"; //"kor"은 object
		String ss2 = new String();
		ss2 = "kor";   			// 문자열은 리터럴 풀에 저장
		String ss3 = new String("kor"); //별도의 heap에 저장
		System.out.println(ss1 + " " + ss2 + " " + ss3);
		
		//주소를 비교하는 것, ss1,2와 ss3은 저장하는 방식이 다름
		if(ss1 == ss2) System.out.println("같음1");
		else System.out.println("다름1");
		if(ss1 == ss3) System.out.println("같음2");
		else System.out.println("다름2");
		if(ss2 == ss3) System.out.println("같음3");
		else System.out.println("다름3");
		
		System.out.println(ss1.hashCode() +" "+ ss2.hashCode() +" "+ ss3.hashCode());
		
		/**문자열 비교용 메소드 equals() : String 객체의 값을 비교
		 * 자바는 문자열 리터럴이 동일하다면 String 객체를 공유하도록 되어있다
		 * but new 연산자를 사용하면 힙에 새로운 객체를 생성 **/
		if(ss1.equals(ss2)) System.out.println("같음1");
		else System.out.println("다름1");
		if(ss1.equals(ss3)) System.out.println("같음1");
		else System.out.println("다름1");
		if(ss2.equals(ss3)) System.out.println("같음1");
		else System.out.println("다름1");
//		if(ss2.equalsIgnoreCase(ss3)) //영어의 경우 영문자 대소 구분 X
		
		
		System.out.println("\n배열 관련");
		int ar1[] = {1,2,3};
		System.out.println(ar1); //ar1의 주소
		
		int[][] ar2 = {{1,2,3}, {4,5,6}};
		System.out.println(ar2);
		System.out.println(ar2[0] + " " + ar2[1]);
	
	}

}
