package pack9;

/****** 스레드 활성화, 비활성화 *****/
public class BreadMain {
	
	public static void main(String[] args) {
		// 두 개 이상의 스레드로 빵 자원을 공유
		BreadPlate breadplate = new BreadPlate();
		BreadMaker maker = new BreadMaker(breadplate);
		BreadEater eater = new BreadEater(breadplate);
		maker.setPriority(8);
		
		maker.start();
		eater.start();
	}
}
