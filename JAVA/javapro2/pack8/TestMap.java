package pack8;

import java.util.HashMap;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

/***** Map 인터페이스 : 자료를 Key, Value 형태로 저장, 많은 양의 데이터인 경우 검색이 편리
 * key값은 중복 불가, value는 중복 가능 *****/
public class TestMap {
	public static void main(String[] args) {
		HashMap<String, String> list = new HashMap<String, String>();
		list.put("0", "lee");
		list.clear();
		list.put("1", "lee");
		list.put("2", "kim");
		list.put("3", "park");
		list.put("4", "lee");
		list.put("5", "choi");
		System.out.println(list.size());
		list.remove("3");
		System.out.println(list.containsKey("0"));
		System.out.println(list.containsValue("kim"));
		
		System.out.println(list);
		System.out.println();
		
		print(list);
	}
	
	public static void print(Map map) {
		Set set = map.keySet();
		Iterator iter = set.iterator(); //나열형 데이터
		System.out.println(iter);
		
		while(iter.hasNext()) {//다음 자료가 있는 경우 동안
			String key = (String)iter.next();
			System.out.println("key : " + key);
			System.out.println("value : " + map.get(key));
		}
	}
}
