package pack8;

import java.util.ArrayList;

/***** DTO 연습 : 레코드형 기억장소 **/
public class TestDto {
	ArrayList<StudentDto> list = new ArrayList<StudentDto>();
	
	public void aa() {
		String[] persons = new String[3];
		persons[0] = "홍길동";
		persons[1] = "고길동";
		persons[2] = "나길동";
		
		for(String s:persons) {
			System.out.println(s);
		}
	}
	
	public void insertData() {
		//학번, 이름, 점수를 레코드 단위로 입력 후 기억
		StudentDto dto = null;
		
		dto = new StudentDto();
		dto.setHakbun("ks1");
		dto.setIrum("홍길동");
		dto.setJumsu(90);
		list.add(dto); //첫번째 학생 자료 기억
		
		dto = new StudentDto(); // 28 line 없이 이렇게 하면 덮어쓰기 될 뿐
		dto.setHakbun("ks2"); // 객체 하나만 이용해서 list에 데이터 저장
		dto.setIrum("고길동");
		dto.setJumsu(80); 
		list.add(dto); // 두번째 기억
		
		dto = new StudentDto();
		dto.setHakbun("ks3"); 
		dto.setIrum("나길동");
		dto.setJumsu(10); 
		list.add(dto); // 세번째 기억
		
		// ... 반복문으로 처리
	}
	
	public void showData() {
		System.out.println("학생 수는 " + list.size() + "명");
		for (int i = 0; i < list.size(); i++) {
			StudentDto dto = new StudentDto();
			dto = list.get(i);
//			System.out.println(dto);// 다 다른 주소
			System.out.println(dto.getHakbun() + " " +  dto.getIrum() + " " + dto.getJumsu());
		}
		
		for(StudentDto d:list) {
			System.out.println(d.getHakbun() + d.getIrum() + d.getJumsu());
		}
	}
	
	/**MAIN**/
	public static void main(String[] args) {
		TestDto test = new TestDto();
		test.aa();
		test.insertData();
		test.showData();
//		System.out.println(test.list.size()); // 3
	}
}
