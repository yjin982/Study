package pack2;

public class ArticleDAO implements ArticleInter{
	//DB처리 관련 클래스(모델쪽)
	
	public void selectAll() {
		System.out.println("ArticleDAO의 selectAll()에서 DB의 고객 전체 자료 읽었다고 가정");
	}
}
