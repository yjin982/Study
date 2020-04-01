package pack;

import java.util.ArrayList;

public class HobbyModel {
	public static HobbyModel model = new HobbyModel();
	
	public static HobbyModel getInstance() {
		return model;
	}
	
	public ArrayList<String> getHobby(String hobby){
		ArrayList<String> list = new ArrayList<String>();
		
		if(hobby.equals("m")) { //원래는 DB에 갔다와야하지만 임시로 대체
			list.add("설악산");
			list.add("한라산");
		}else if(hobby.equals("t")) {
			list.add("남해안");
			list.add("동해안");
			list.add("서해안");
		}else if(hobby.equals("s")) {
			list.add("수영장");
		}else if(hobby.equals("r")) {
			list.add("마라톤");
			list.add("경보");
		}
		
		return list;
	}
}
