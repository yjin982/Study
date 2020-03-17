package pack;

public class ExamProcess {
//	private String name;
//	private int kor;
//	private int eng;
	
	//getter, setter를 만들어 운영할 수도 있으나 레코드 단위의 처리로 실습. FormBean을 사용.
	private ExamBean examBean;
	
	public void setExamBean(ExamBean examBean) {
		this.examBean = examBean;
	}
	
	public int getTot() {
		return examBean.getKor()+examBean.getEng();
	}
	public double getAvg() {
		return getTot() / 2.0;
	}
}
