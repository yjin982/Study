package pack5;

public class PolyProductMain {
	public static void main(String[] args) {
		//다형성 연습
		PolyProduct product = null;
		
		PolyRadio radio = new PolyRadio();
		radio.setVolume(6);
		radio.volumeControl();
		
		System.out.println();
		
		PolyTv tv = new PolyTv();
		tv.setVolume(10);
		tv.volumeControl();
		tv.tvShow();
		
		System.out.println("=====다형성=====");
		product = radio;
		product.volumeControl();
		product = tv;
		product.setVolume(15);
		product.volumeControl();
//		product.tvShow();
		
		System.out.println();
		
		PolyProduct[] p = new PolyProduct[2];
		p[0] = radio;
		p[1] = tv;
		for(PolyProduct abc:p) {
			abc.volumeControl();
		}
		
	}
}
