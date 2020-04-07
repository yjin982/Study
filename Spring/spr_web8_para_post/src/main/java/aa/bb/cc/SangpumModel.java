package aa.bb.cc;

import org.springframework.stereotype.Repository;

@Repository
public class SangpumModel {
	
	public String computeData(SangpumBean bean) {
		String data = "품명 : " + bean.getSang() + ", 금액 : " + (bean.getSu() * bean.getDan());		
		return data;
	}
}
