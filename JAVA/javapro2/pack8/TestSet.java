package pack8;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Set;

/***** Set 인터페이스 : 중복불가, 순서 없음 *****/
public class TestSet {
	public static void main(String[] args) {
		/*HashSet list = new HashSet<Object>(); // == HashSet<Object> 으로 쓴 것과 동일
		list.add("lee");
		list.add(1); //  = Boxing <-> UnBoxing
		
		TestSet ts = new TestSet();
		list.add(ts); //object이기 때문에 ts도 가능*/
		
		HashSet<String> list = new HashSet<String>();
//		list.add(1);//제네릭을 String으로 제한해서 문자열만 들어감
		list.add("lee"); 
		list.add("kim");
		list.add("lee");
		list.add("park");
		list.add("choi");
		System.out.println(list.size()); //중복 허용 X
		
		list.remove("kim");
		System.out.println(list.size());
		
		System.out.println(list); //주소가 아니라 값이 출력
		System.out.println(list.toString());
//		System.out.println(list[0]);// X
		
		print(list); System.out.println("--");
		print2(list.toArray());
		
	}
	
	public static void print(Set set) {
		Iterator iter = set.iterator(); //나열형 데이터
		System.out.println(iter);
		
		while(iter.hasNext()) {//다음 자료가 있는 경우 동안
			String ss = (String)iter.next();
			System.out.println(ss);
		}
	}
	
	public static void print2(Object[] obj) {
		int count = obj.length;
		
		for (int i = 0; i < count; i++) {
			System.out.println(obj[i]);
		}System.out.println();
		
		//향상된 for문
		for(Object aa:obj) {
			System.out.println((String)aa);
		}
//		for(String s : obj) {
//			System.out.println(s);
//		}
	}
}
