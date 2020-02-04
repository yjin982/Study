package pack8;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

/***** List 인터페이스 : 중복 가능, 순서 있음 *****/
public class TestList {
	public static void main(String[] args) {
		ArrayList<String> list = new ArrayList<String>();
		list.add("kim");
		System.out.println(list.size());
		
		list.clear();
		System.out.println(list.size());
		
		list.add("kim");
		list.add("lee"); 
		list.add("park");
		list.add("kim");
		list.add("choi");
		list.remove("lee");
		list.remove(0);
		System.out.println(list.size());
		System.out.println(list);
//		System.out.println(list[0]);
		System.out.println(list.get(0));
		System.out.println(list.contains("park"));
		
		System.out.println();
		print(list); System.out.println();		
		print2(list);
		
	}
	
	public static void print(List list) {
		Iterator iter = list.iterator(); //나열형 데이터
		System.out.println(iter);
		
		while(iter.hasNext()) {//다음 자료가 있는 경우 동안
			String ss = (String)iter.next();
			System.out.println(ss);
		}
	}
	
	public static void print2(List obj) {
		for(Object aa:obj) {
			System.out.println((String)aa);
		}
//		for(String s : obj) {
//			System.out.println(s);
//		}
	}
}
