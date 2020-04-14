package pack.model;

import java.util.List;

public interface JikwonInter {
	List<JikwonDto> jikwonList();
	JikwonDto getLoginInfo(String no);
}
