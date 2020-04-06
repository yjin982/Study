package pack.business;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.stereotype.Service;

import pack.model.DataDto;
import pack.model.SangpumInter;

@Service
@ComponentScan("pack.model")
public class BusinessImpl implements BusinessInter{
	@Autowired  // java의 @Resources는 이름에 의한 mapping
	@Qualifier("sangpumImpl")
	private SangpumInter inter;
	
	public void dataList() {
		List<DataDto> list = inter.selectDataAll();
		
		//출력
		for(DataDto dto : list) {
			System.out.println(dto.getCode() + " " + dto.getSang() + " " + dto.getSu() + " " + dto.getDan());
		}
	}
}
