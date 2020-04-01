package pack;

import java.util.List;

public class Main {

	public static void main(String[] args) {
		ProcessDao dao = new  ProcessDao();
		
		
		try {
//			System.out.println("-------상품 추가");
//			DataDto dto = new DataDto();
//			dto.setCode("100");
//			dto.setSang("바나나우유");
//			dto.setSu("10");
//			dto.setDan("2000");
//			dao.insData(dto);//한번만 실행해야
			
			System.out.println("-------상품 수정");
			DataDto dto = new DataDto();
			dto.setCode("5");
			dto.setSang("유리컵");
			dao.upData(dto);
			
			System.out.println("-------상품 삭제");
			boolean b = dao.deleteData(100);
			if(b) {
				System.out.println("삭제 성공");
			}else {
				System.out.println("삭제 실패");
			}
			
			System.out.println("------전체 자료 출력");
			List<DataDto> list = dao.selectSangDataAll(); //자바 안에서 sql문을 빼낸
			for(DataDto s:list) {
				System.out.println(s.getCode() + " " + s.getSang() + " " + s.getSu() + " " + s.getDan());
			}
			
			
			System.out.println("-------부분 자료 읽기");
			DataDto dataDto = dao.selectDataPart("1");
			System.out.println(dataDto.getCode() + " " + dataDto.getSang() + " " + dataDto.getSu() + " " + dataDto.getDan());
	
			
			
		} catch (Exception e) {
			System.out.println("main err");
			e.printStackTrace();
		}
		

	}

}
