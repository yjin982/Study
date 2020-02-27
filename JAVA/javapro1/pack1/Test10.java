package pack1;

public class Test10 {

	public static void main(String[] args) {
		/*************다중 for, etc***************/
		for (int i = 0; i < 3; i++) {
			System.out.println("i:" + i);
			for (int j = 0; j < 4; j++) {
				System.out.print("j=" + j + " ");
			}
			System.out.println();
		}
		System.out.println();
		
		for(char i = 65; i<91; i++) {
			System.out.print((char)i + " : ");
			for(char j=i; j<91; j++) {
				System.out.print((char)j);
			}
			System.out.println();
		}
		System.out.println();
		
		/*************continue, break***************/
		for(int i = 1; i<=10; i++) {
			if(i==3) continue;
			System.out.println(i);
			// if(i==5) System.exit(0); //프로그램종료
			// if(i==5) return; //메소드탈출
			if(i == 5) break;
			System.out.println("nice");
		}
		System.out.println();
		
		int kk = 0;
		for(;;) {
			kk++; 
			if(kk == 5) break;
		}
		
		/*************label이 있는 경우***************/
		kbs:for(int i=0; i<3; i++) {
			mbc:for(int j=0; j<5; j++) {
				System.out.print(i + " " + j + " ");
				if (j == 3) continue kbs;
				if (j == 4) break kbs;
			}
			System.out.println();
		}
		System.out.println();
		
		
		System.out.println("프로그램 종료");
	}

}
