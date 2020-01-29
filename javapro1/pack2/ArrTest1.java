package pack2;

public class ArrTest1 {

	public static void main(String[] args) {
		/**배열(Array) 성격과 크기가 일치하는 여러 개의 기억장소에 대해 대표명을 주고 첨자로 각 기억장소를 구분하는 방법
		 * 반복처리가 효과적 **/
		System.out.println("/*****배열******/");
//		int[] ar; // == int ar[];
//		ar = new int[5]; //배열 기억장소를 확보
		int ar[] = new int[5]; //선언과 확보 동시에, 1차원 배열
		
		System.out.println("ar의 크기 : " + ar.length);
		
		ar[0] = 10; ar[1] = 20; 	ar[4] = ar[0] + ar[1]; //index로 구분
		
		System.out.println("ar[4] : " + ar[4]);
		System.out.println("ar[3] : " + ar[3]); //배열 초기값을 안 주면 0
//		System.out.println(ar[5]); //ArrayIndexOutOfBoundsException
		
		int a = 4, b = 4;
		System.out.println(ar[4] + " " + ar[a] + " " +ar[b] + " " + ar[1+3] + "\n");
		
		int[] ar1 = {1,2,3,4,5}; //배열 선언 및 초기값 설정
		for (int i = 0; i < ar1.length; i++) {
			System.out.print("ar1[" + i + "] : " + ar1[i] + " ");
		}System.out.println();
		
		for(int i:ar1) { //향상된 for문 - 객체 자료를 출력시 사용 가능
			System.out.print(i + " ");
		}System.out.println();
		
		String[] city = {"서울", "인천", "수원", "판교", "분당"};
		for (String c:city) {
			System.out.print(c + " ");
		}System.out.println();
		
		int[] ar2 = new int[5];
		for (int i = 0; i < ar2.length; i++) {
			ar2[i] = i+1;
		}
		
		int tot = 0;
		for (int i = 0; i < ar2.length; i++) {
			System.out.print("ar2[" + i + "] : " + ar2[i] + " ");
			tot += i;
		}
		System.out.println("=> tot : "+ tot + "\n");
		
		/*****다차원 배열******/
		System.out.println("/*****다차원 배열******/");
		int su[][] = new int[3][4]; //2차원 배열 [행][열]
		System.out.println(su.length + " " + su[0].length); //행의 갯수,열의 갯수
		
		int num = 10;
		for (int i = 0; i < su.length; i++) {
			//System.out.print("i : " + i + " / ");
			for (int j = 0; j < su[i].length; j++) {
				//System.out.print(" j : "+ j + " ");
				su[i][j] = num++;
			}//System.out.println();
		}
		System.out.println(su[0][0]);
		
		for (int m = 0; m < 3; m++) {
			for (int n = 0; n < 4; n++) {
				System.out.print(su[m][n] + " ");
			}System.out.println();
		}
		
		/*****가변 배열******/
		System.out.println("/*****가변 배열******/");
		int[][] scores = new int[2][];
		scores[0] = new int[2];
		scores[1] = new int[3];
		System.out.println(scores.length + " " + scores[0].length + " " + scores[1].length);
		
		int[][] jum = {{90,96}, {89,87,85}};
		for (int i = 0; i < jum.length; i++) {
			for (int j = 0; j < jum[i].length; j++) {
				System.out.print(jum[i][j] + " ");
			}System.out.println();
		}
		
		
	}

}
