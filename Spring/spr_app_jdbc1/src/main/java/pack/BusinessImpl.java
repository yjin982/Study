package pack;

public class BusinessImpl implements BusinessInter{
	private SangpumInter sangpumInter;
	
	public void setSangpumInter(SangpumInter sangpumInter) {
		this.sangpumInter = sangpumInter;
	}
	
	public void dataList() {
		for (SangpumDto dto : sangpumInter.selectList()) {
			System.out.println(dto.getCode() + " " + dto.getSang() + " " + dto.getSu() + " " + dto.getDan());
		}
	}
}
