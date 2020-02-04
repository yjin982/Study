package pack8;

import java.util.ArrayList;
import java.util.Calendar;
import java.util.StringTokenizer;

public class TestDto2 {
	ArrayList<HanksaengDto> list;
	
	public TestDto2() {
		list = new ArrayList<HanksaengDto>();
	}
	
	
	
	public void inputData(String[] datas) {
		for (int i = 0; i < datas.length; i++) {
			StringTokenizer tok = new StringTokenizer(datas[i], ",");
			String irum = tok.nextToken();
			int kor = Integer.parseInt(tok.nextToken());
			int eng = Integer.parseInt(tok.nextToken());
			int mat = Integer.parseInt(tok.nextToken());
			
			HanksaengDto dto = new HanksaengDto();
			dto.setName(irum);
			dto.setKor(kor);
			dto.setEng(eng);
			dto.setMat(mat);
			list.add(dto);
		}
	}
	public void displayData() {
		for (int i = 0; i < list.size(); i++) {
			HanksaengDto dto = new HanksaengDto();
			dto = list.get(i);
			int tot = dto.getKor() + dto.getEng() + dto.getMat();
			double avg = tot / 3;
			System.out.println(dto.getName() + " "+ tot + " "+ Math.round(avg));
		}System.out.println();
		
		
		//향상된 for
		for(HanksaengDto dto:list) {
			int tot = dto.getKor() + dto.getEng() + dto.getMat();
			double avg = tot / 3;
			System.out.println(dto.getName() + " "+ tot + " "+ Math.round(avg));
		}
		
	}

	/**MAIN**/
	public static void main(String[] args) {
		//문자열 분리 클래스
		String da = "kbs,mbc";
		StringTokenizer tokenizer = new StringTokenizer(da, ",");
		String s1 = tokenizer.nextToken();
		String s2 = tokenizer.nextToken();
		System.out.println(s1 + " " + s2 + " \n");
		
		String[] datas = new String[3];
		datas[0] = "공깃밥,100,100,100";
		datas[1] = "김밥,80,90,88";
		datas[2] = "주먹밥,77,88,66";
		
		TestDto2 test2 = new TestDto2();
		test2.inputData(datas); //입력
		test2.displayData();		  //출력
		
		
		//참고 년월일 구하기
		Calendar c = Calendar.getInstance();
		int year = c.get(Calendar.YEAR);
		int month = c.get(Calendar.MONTH) + 1; //month가 0부터 출발해서
		int day = c.get(Calendar.DATE);
		System.out.println(year + "." + month + "." + day);
	}
}
