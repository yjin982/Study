package pack2;

public class LogicImpl implements LogicInter{
	//핵심 로직
	private ArticleInter articleInter;
	
	public LogicImpl() {}
	public LogicImpl(ArticleInter articleInter) {
		this.articleInter = articleInter;
	}
	
	public void selectDataProcess() {
		articleInter.selectAll();
	}
	
	public void updateDataPart() {
		System.out.println("updateDataPart 수행");
	}
	
	public void etc() {
		System.out.println("다른 작업이 더 있을 수 있음");
	}
}
