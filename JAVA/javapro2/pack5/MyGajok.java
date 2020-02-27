package pack5;

public class MyGajok {
	public static void main(String[] args) {
		/**상속 연습**/
		GrandFa gr = new GrandFa();
		System.out.println("가보 : "+gr.gabo);
		System.out.println("가훈 : "+gr.gahun); //같은 패키지 내에서는 public 같이
		System.out.println(gr.say());
		gr.eat();
		System.out.println("할아버지 나이 : " + gr.getNai());
		System.out.println();
		
		GrandFa gr2 = new GrandFa(82);
		System.out.println(gr2.say());
		System.out.println("할아버지2 나이 : " + gr2.getNai());
		System.out.println();
		
		System.out.println("______아버지______");
		Father fa = new Father();
		System.out.println("가보 : "+fa.gabo);
		System.out.println("가훈 : "+fa.gahun);
		System.out.println(fa.say());
		fa.eat();
		System.out.println("아버지 나이 : " + fa.getNai());
		System.out.println(" - ");
		fa.showData();
		System.out.println();
		
		System.out.println("______나______");
		Me me = new Me();
		me.Biking();
		System.out.println(me);
		System.out.println("가보 : "+me.gabo);
		System.out.println("가훈 : "+me.gahun);
		System.out.println(me.say());
		me.eat();
		System.out.println("내 나이 : " + me.getNai());
		System.out.println(" - ");
		me.showData();
		

	}
}
